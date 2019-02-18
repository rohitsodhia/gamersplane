<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

use App\Models\TestSubModel;

class TestModel extends Eloquent
{

	protected $connection = 'mongo';
	protected $guarded = [];

	public function subs() {
		return $this->embedsOne('App\Models\TestSubModel');
	}

}
