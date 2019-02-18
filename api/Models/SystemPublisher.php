<?php

namespace App\Models;

class SystemPublisher extends \phpDM\Models\MongoModel
{

	protected static $fields = [
		'name' => 'string',
		'site' => 'string'
	];

}
