<?php

namespace App\Models;

use \Exception;

use phpDM\Models\MongoModel;

class PM extends MongoModel
{

	protected static $collection = 'pms';
	static protected $primaryKey = 'pmID';
	protected static $fields = [
		'_id' => 'mongoId',
		'pmID' => 'int',
		'sender' => [
			'type' => 'object',
			'fields' => [
				'userID' => 'int',
				'username' => 'str',
			]
		],
		'recipients' => 'array(\App\Models\PMRecipient)',
		'title' => 'str',
		'message' => 'str',
		'datestamp' => 'createdTimestamp',
		'replyTo' => 'int',
		'history' => 'array(int)',
	];

}
