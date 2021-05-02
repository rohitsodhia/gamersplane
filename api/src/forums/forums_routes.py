from flask import Blueprint, request

from helpers.response import response

from forums.models import Forum
from forums.serializers import ForumSerializer
from helpers.cache import CacheKeys, get_objects_by_id

forums = Blueprint("forums", __name__, url_prefix="/forums")


@forums.route("/<forum_id>", methods=["GET"])
def get_forums(forum_id: int = 0):
    forum = get_objects_by_id(forum_id, Forum, CacheKeys.FORUM_DETAILS.value)
    serialized_forum = ForumSerializer(forum)

    return response.success(data={"forum": serialized_forum.data})
