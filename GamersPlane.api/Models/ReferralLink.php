<?php

namespace App\Models;

use phpDM\Models\MysqlModel;

class ReferralLink extends MysqlModel
{

	static protected $primaryKey = 'key';
	protected static $fields = [
		'key' => 'string',
		'title' => 'string',
		'link' => 'str',
		'order' => 'int',
	];

}
