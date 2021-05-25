from flask import Blueprint, request

from helpers.response import response
from helpers.endpoint import require_values
from helpers.cache import CacheKeys, get_objects_by_id

from forums.models import Forum
from forums.serializers import ForumSerializer
from games.models import Game

forums = Blueprint("forums", __name__, url_prefix="/forums")


@forums.route("/<int:forum_id>", methods=["GET"])
def get_forums(forum_id: int = 0):
    forum = get_objects_by_id(forum_id, Forum, CacheKeys.FORUM_DETAILS.value)
    serialized_forum = ForumSerializer(forum)

    return response.success(data={"forum": serialized_forum.data})


@forums.route("", methods=["POST"])
def create_forum():
    request_data = request.json
    fields_missing = require_values(request_data, ["title", "forumType", "parent"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})
    invalid_values = {}
    if request_data["forumType"] not in Forum.ForumTypes.values:
        invalid_values[
            "forum_type"
        ] = f"forumTypes must be in [{Forum.ForumTypes.values}])"
    if not int(request_data["parent"]):
        invalid_values["parent"] = f"parent must be an integer"
    parent: Forum = get_objects_by_id(
        request_data["parent"], Forum, CacheKeys.FORUM_DETAILS.value
    )
    if not parent:
        invalid_values["parent"] = f"parent \"{request_data['parent']}\" does not exist"

    game = None
    if "game_id" in request_data:
        game: Game = get_objects_by_id(
            request_data["game_id"], Game, CacheKeys.GAME_DETAILS.value
        )
        if not game:
            invalid_values[
                "game_id"
            ] = f"game_id \"{request_data['game_id']}\" does not exist"
    if invalid_values:
        return response.errors({"invalid_values": invalid_values})

    forum_values = {
        "title": request_data["title"],
        "forumType": request_data["forumType"],
        "parent": parent,
    }
    if "description" in request_data:
        forum_values["description"] = request_data["description"]
    if game:
        forum_values["game"] = game

    forum = Forum(**forum_values)
    forum.save()
    forum.generate_heritage()
    forum.save()
    return response.success({"forum": {"id": forum.id, "title": forum.title}})
