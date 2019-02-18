<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\SoftDeletes;

class Usermeta extends Model
{

	protected $table = 'usermeta';
	protected $primaryKey = 'metaID';
	public $timestamps = false;

	protected $guarded = ['metaID'];

	public function __toString()
	{
		return $this->metaValue;
	}

	public function getMetaValueAttribute($value)
	{
		if (is_string($value) && strlen($value) > 4 && substr($value, 0, 2) == 'a:') {
			$value = unserialize($value);
		}
		return $value;
	}

	public function setMetaValueAttribute($value)
	{
		if (is_array($value)) {
			$this->attributes['metaValue'] = serialize($value);
		} else {
			$this->attributes['metaValue'] = $value;
		}
	}

	public function user() {
		return $this->belongsTo(User::class, 'userID');
	}

}
