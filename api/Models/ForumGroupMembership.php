<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class ForumGroupMembership extends Model
{
	protected $connection = 'mongo';

	protected $collection = 'forums_groupMemberships';
	public $timestamps = false;
	protected $guarded = [];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (ForumGroupMembership $forumGroupMembership) {
		});
	}
}
