from flask import Blueprint, request

from helpers.response import response
from helpers.endpoint import require_values

from users.models import User

users = Blueprint("users", __name__, url_prefix="/users")


@users.route("/<id>", methods=["GET"])
def get_user(id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return response.errors({"noUser": True})
    return response.success({"user": user.to_dict()})
