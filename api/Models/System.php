<?php

namespace App\Models;

use phpDM\Models\MongoModel;

class System extends MongoModel
{

	protected static $fields = [
		'_id' => 'string',
		'name' => 'string',
		'sortName' => 'string',
		'publisher' => 'object:\App\Models\SystemPublisher',
		'genres' => 'array(string)',
		'lfg' => 'integer',
		'hasCharSheet' => 'bool',
		'enabled' => 'bool'
	];

}
