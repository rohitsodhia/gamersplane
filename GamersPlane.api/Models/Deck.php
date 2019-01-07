<?php

namespace App\Models;

use phpDM\Models\MysqlModel;

class Deck extends MysqlModel
{

	static protected $primaryKey = 'deckID';
	protected $fields = [
		'deckID' => 'bool',
		'label' => 'str',
		'type' => 'str',
		'deck' => 'array(int)',
		'position' => 'int',
		'lastShuffle' => 'timestamp',
		'permissions' => 'array(int)',
	];

}
