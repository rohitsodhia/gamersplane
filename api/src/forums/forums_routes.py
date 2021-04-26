from flask import Blueprint, request
from django.core.cache import cache

from helpers.response import response
from helpers.cache import CACHE_KEYS

from forums.models import Forum
from forums.serializers import ForumSerializer

forums = Blueprint("forums", __name__, url_prefix="/forums")


@forums.route("/<forum_id>", methods=["GET"])
def get_forums(forum_id: int = 0):
    forum_cache = cache.get(CACHE_KEYS["forum_details"].format(forum_id=forum_id))
    if forum_cache:
        forum = forum_cache
    else:
        forum = Forum.objects.get(id=forum_id)
    cache.set(CACHE_KEYS["forum_details"].format(forum_id=forum_id), forum)

    serialized_forum = ForumSerializer(forum)

    return response.success(data={"forum": serialized_forum.data})
