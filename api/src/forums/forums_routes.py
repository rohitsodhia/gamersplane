from flask import Blueprint, request

from helpers.response import response

from forums.models.forum import get_forums_by_id
from forums.serializers import ForumSerializer

forums = Blueprint("forums", __name__, url_prefix="/forums")


@forums.route("/<forum_id>", methods=["GET"])
def get_forums(forum_id: int = 0):
    forum = get_forums_by_id(forum_id)
    serialized_forum = ForumSerializer(forum)

    return response.success(data={"forum": serialized_forum.data})
