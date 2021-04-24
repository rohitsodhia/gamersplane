from flask import Blueprint, request
from django.core.cache import cache

from helpers.response import response

from forums.models import Forum

forums = Blueprint("forums", __name__)


@forums.route("/{forum_id}", methods=["GET"])
def get_forums(forum_id: int = 0):
    forum_cache = cache.get(f"forum:{forum_id}:details")
    if forum_cache:
        forum = Forum(**forum_cache)
    else:
        forum = Forum().objects.get(forum_id)
