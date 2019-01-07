<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class ForumPermission extends Model
{
	protected $connection = 'mongo';

	protected $collection = 'forums_permissions';
	public $timestamps = false;
	protected $guarded = [];

	const TYPE_VALUES = [
		'general' => 1,
	 	'group' => 2,
	 	'user' => 4
	];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (ForumPermission $forumPermission) {
		});
	}

	protected function accessPermission($value)
	{
		$value = (int) $value;
		if ($value > 0) {
			return self::TYPE_VALUES[$this->type];
		} elseif ($value < 0) {
			return -1 * self::TYPE_VALUES[$this->type];
		} else {
			return 0;
		}
	}

	protected function mutatePermission($value)
	{
		$value = (int) $value;
		if ($value > 0) {
			return 1;
		} elseif ($value < 0) {
			return -1;
		} else {
			return 0;
		}
	}

	public function getReadAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setReadAttribute($value)
	{
		$this->attributes['read'] = $this->mutatePermission($value);
	}

	public function getWriteAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setwriteAttribute($value)
	{
		$this->attributes['write'] = $this->mutatePermission($value);
	}

	public function getEditPostAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setEditPostAttribute($value)
	{
		$this->attributes['editPost'] = $this->mutatePermission($value);
	}

	public function getDeletePostAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setDeletePostAttribute($value)
	{
		$this->attributes['deletePost'] = $this->mutatePermission($value);
	}

	public function getCreateThreadAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setCreateThreadAttribute($value)
	{
		$this->attributes['createThread'] = $this->mutatePermission($value);
	}

	public function getDeleteThreadAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setDeleteThreadAttribute($value)
	{
		$this->attributes['deleteThread'] = $this->mutatePermission($value);
	}

	public function getAddPollAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setAddPollAttribute($value)
	{
		$this->attributes['addPoll'] = $this->mutatePermission($value);
	}

	public function getAddRollsAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setAddRollsAttribute($value)
	{
		$this->attributes['addRolls'] = $this->mutatePermission($value);
	}

	public function getAddDrawsAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setAddDrawsAttribute($value)
	{
		$this->attributes['addDraws'] = $this->mutatePermission($value);
	}

	public function getModerateAttribute($value)
	{
		return $this->accessPermission($value);
	}

	public function setModerateAttribute($value)
	{
		$this->attributes['moderate'] = $this->mutatePermission($value);
	}
}
