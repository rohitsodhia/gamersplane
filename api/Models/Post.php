<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class Post extends Model
{
	protected $connection = 'mongo';

	public $primaryKey = 'postId';
	public $timestamps = false;
	protected $guarded = [];

	protected $dates = ['datePosted', 'lastEdit'];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (Post $post) {
		});
	}

	public function lastPost()
	{
		return $this->embedsOne('App\Models\LastPost');
	}
}
