import json

from flask import Blueprint, request

from helpers.decorators import logged_in
from helpers.response import response
from helpers.endpoint import require_values

from roles.models import Role

roles = Blueprint("roles", __name__, url_prefix="/roles")


@roles.route("/", methods=["GET"])
@logged_in(permissions=["viewRoles"])
def list_roles():
    roles = Role.objects.all()
    return response.success({"roles": roles})
