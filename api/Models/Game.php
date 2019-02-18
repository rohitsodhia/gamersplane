<?php

namespace App\Models;

use phpDM\Models\MongoModel;

class Game extends MongoModel
{

	static protected $primaryKey = '_id';
	protected static $fields = [
		'_id' => 'mongoId',
		'gameId' => 'int',
		'title' => 'str',
		'system' => 'str',
		'created' => 'createdTimestamp',
		'start' => 'timestamp',
		'end' => 'timestamp',
		'retired' => 'timestamp',
		'postFrequency' => [
			'type' => 'object',
			'fields' => [
				'timesPer' => 'int',
				'perPeriod' => 'str',
			]
		],
		'numPlayers' => 'int',
		'charsPerPlayer' => 'int',
		'description' => 'str',
		'charGenInfo' => 'str',
		'status' => 'str',
		'public' => 'bool',
		'groupId' => 'int',
		'forumId' => 'int',
		'gm' => [
			'type' => 'object',
			'fields' => [
				'userId' => 'int',
				'username' => 'str',
			]
		],
		'allowedCharSheets' => 'array(str)',
		'players' => 'array(object:\App\Models\GamePlayer)',
		'decks' => 'array(object:\App\Models\Deck)',
	];

}
