<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model as Eloquent;

class TestSubModel extends Eloquent
{

	protected $connection = 'mongo';
	protected $guarded = [];

}
