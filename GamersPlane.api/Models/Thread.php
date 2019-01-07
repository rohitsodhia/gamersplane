<?php

namespace App\Models;

use Jenssegers\Mongodb\Eloquent\Model;

class Thread extends Model
{
	protected $connection = 'mongo';

	public $primaryKey = 'threadId';
	public $timestamps = false;
	protected $guarded = [];

	protected $dates = ['datePosted', 'lastEdit'];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (Thread $thread) {
		});
	}

	public function lastPost()
	{
		return $this->embedsOne('App\Models\LastPost');
	}
}
