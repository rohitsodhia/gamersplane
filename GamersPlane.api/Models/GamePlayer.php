<?php

namespace App\Models;

use phpDM\Models\GenericModel;

class GamePlayer extends GenericModel
{

	protected $parent = '\phpDM\Models\MongoModel';
	protected $fields = [
		'user' => [
			'type' => 'object',
			'fields' => [
				'userId' => 'int',
				'username' => 'str',
			]
		],
		'isGM' => 'bool',
		'approved' => 'bool',
	];

}
