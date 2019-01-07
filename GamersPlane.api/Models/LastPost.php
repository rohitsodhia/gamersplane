<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class LastPost extends Model
{
	protected $connection = 'mongo';

	public $primaryKey = 'postId';
	public $timestamps = false;
	protected $guarded = [];

	protected $dates = ['datePosted'];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (LastPost $LastPost) {
		});
	}
}
