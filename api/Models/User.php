<?php

namespace App\Models;

use \Exception;

use phpDM\Models\MysqlModel;

class User extends MysqlModel
{

	static protected $primaryKey = 'userID';
	protected static $fields = [
		'userID' => 'int',
		'username' => 'str',
		'password' => 'str',
		'salt' => 'str',
		'email' => 'str',
		'joinDate' => 'createdTimestamp',
		'activatedOn' => 'timestamp',
		'lastActivity' => 'timestamp',
		'reference' => 'str',
		'enableFilter' => 'bool',
		'showAvatars' => 'bool',
		'avatarExt' => 'str',
		'timezone' => 'str',
		'showTZ' => 'bool',
		'realName' => 'str',
		'gender' => 'str',
		'birthday' => 'timestamp',
		'showAge' => 'bool',
		'location' => 'str',
		'aim' => 'str',
		'gmail' => 'str',
		'twitter' => 'str',
		'stream' => 'str',
		'games' => 'str',
		'newGameMail' => 'bool',
		'postSide' => 'str',
		'suspendedUntil' => 'timestamp',
		'banned' => 'bool',
		'deleted' => 'deletedTimestamp',
	];

	public static function validUsername($username)
	{
		return strlen($username) >= 4 && strlen($username) <= 24 && preg_match('/[a-z][a-z0-9\._]{3,23}/i', $username);
	}

	public static function validPassword($password)
	{
		return strlen($password) >= 8;
	}

	protected function setPassword($password) {
		$this->data['password'] = static::hashPassword($password);
	}

	public static function hashPassword($password)
	{
		return password_hash($password, PASSWORD_DEFAULT);
	}

	public function validatePassword($password) {
		if (strlen($this->password) === 60) {
			return password_verify($password, $this->password);
		} else {
			return hash('sha256', env('PVAR') . $password . $this->salt) === $this->password;
		}
	}

	public function sendActivationEmail() {
		if (env('APP_ENV') !== 'local') {
			$message = "Thank you for registering for Gamers Plane!\n\n";
			$message .= "Please click on the following link to activate your account:\n";
			$message .= '<a href="https://gamersplane.com/register/activate/' . md5($this->username) . "\">Activate account</a>\n";
			$message .= 'Or copy and paste this URL into your browser: https://gamersplane.com/register/activate/' . md5($this->username) . "/\n\n";
			do {
				$mailSent = mail($this->email, 'Gamers Plane Activation Required', $message, 'From: contact@gamersplane.com');
			} while (!$mailSent);
		}
	}

	public function getJWT()
	{
		$signer = new \Lcobucci\JWT\Signer\Hmac\Sha256();
		$now = time();
		$token = (new \Lcobucci\JWT\Builder())
			->setIssuer(env('APP_DOMAIN'))
			->setIssuedAt($now)
			->setExpiration($now + 60 * 60 * 24 * 7 * (env('APP_ENV') === 'local' ? 52 : 1))
			->set('userId', $this->userID)
			->set('username', $this->username)
			->set('avatar', static::getAvatar($this->userID))
			->sign($signer, env('JWT_SECRET'))
			->getToken();

		return (string) $token;
	}

	static function getAvatar($userID, $ext = false, $exists = false)
	{
		$userID = (int) $userID;
		if ($userID <= 0) {
			return $exists ? false : null;
		}

		if (!$ext) {
			$ext = User::getQueryBuilder()->table('usermeta')->select('metaValue')->where('userID', $userID)->where('metaKey', 'avatarExt')->limit(1)->get();
			if ($ext) {
				$ext = $ext->metaValue;
			} else {
				$ext = false;
			}
		}
		if ($ext !== false && file_exists(env('FILEROOT') . "/assets/images/avatars/{$userID}.{$ext}")) {
			return $exists ? true : env('APP_DOMAIN') . "/assets/images/avatars/{$userID}.{$ext}";
		} else {
			return $exists ? false : null;
		}
	}

	public function checkACP($role, $redirect = true)
	{
		if ($role == 'all' && sizeof($this->acpPermissions)) {
			return $this->acpPermissions;
		} elseif ($role == 'any' && sizeof($this->acpPermissions)) {
			return true;
		} else {
			if (!$redirect && ($this->acpPermissions == null || (!in_array($role, $this->acpPermissions) && !in_array('all', $this->acpPermissions)))) {
				return false;
			} elseif ($this->acpPermissions == null) {
				header('Location: /');
				exit;
			} elseif (!in_array($role, $this->acpPermissions) && !in_array('all', $this->acpPermissions)) {
				header('Location: /acp/');
				exit;
			} else {
				return true;
			}
		}
	}

	static public function inactive($lastActivity, $returnImg = true)
	{
		$diff = time() - strtotime($lastActivity);
		$diff = floor($diff / (60 * 60 * 24));
		if ($diff < 14) {
			return false;
		}
		$diffStr = 'Inactive for';
		if ($diff <= 30) {
			$diffStr .= ' '.($diff - 1).' days';
		} else {
			$diff = floor($diff / 30);
			if ($diff < 12) {
				$diffStr .= ' ' . $diff . ' months';
			} else {
				$diffStr .= 'ever!';
			}
		}
		return $returnImg ? "<img src=\"/images/sleeping.png\" title=\"{$diffStr}\" alt=\"{$diffStr}\">" : $diffStr;
	}
}
