<?php

namespace App\Models;

use Illuminate\Support\Facades\DB;

use Jenssegers\Mongodb\Eloquent\Model;

use App\ForumPermissionsManager;

class Forum extends Model
{
	protected $connection = 'mongo';

	public $primaryKey = 'forumId';
	public $timestamps = false;
	protected $guarded = [];

	protected static function boot()
	{
		parent::boot();
		static::creating(function (Forum $forum) {
		});
	}

	public function lastPost()
	{
		return $this->embedsOne('App\Models\LastPost');
	}

	public function getThreads(int $page = null, int $numItems = null)
	{
		if ($this->type !== 'f') {
			return null;
		}
		if ($page === null || $page <= 0) {
			$page = 1;
		}
		if ($numItems === null || $numItems < 10) {
			$numItems = getenv('PAGINATE_PER_PAGE');
		}

		$threads = Thread::where('forumId', $this->forumId)
			->orderBy('datePosted', 'desc')
			->when($page > 1, function ($query) use ($page) {
				return $query->skip(($page - 1) * $numItems);
			})
			->take($numItems)
			->get();
		$threadCount = Thread::where('forumId', $this->forumId)->count();

		return ['threads' => $threads, 'count' => $threadCount];
	}
}
