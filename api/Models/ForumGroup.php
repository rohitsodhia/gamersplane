<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class ForumGroup extends Model
{
	protected $connection = 'mongo';

	protected $collection = 'forums_groups';
	public $timestamps = false;
	protected $guarded = [];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (ForumGroup $forumGroup) {
		});
	}
}
