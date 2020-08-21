import json

from flask import Blueprint, request

from helpers.decorators import logged_in
from helpers.response import response
from helpers.endpoint import require_values

from auth.models import User

roles = Blueprint("roles", __name__, url_prefix="/roles")


@roles.route("/", methods=["PATCH"])
@logged_in
def list_roles():
    pass
