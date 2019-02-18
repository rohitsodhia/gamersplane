<?php

namespace App\Models;

use \Exception;

use phpDM\Models\GenericModel;

class PMRecipient extends GenericModel
{

	protected $parent = '\phpDM\Models\MongoModel';
	protected static $fields = [
		'userID' => 'int',
		'username' => 'str',
		'read' => 'bool',
		'deleted' => 'bool'
	];

}
