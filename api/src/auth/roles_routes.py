import json

from flask import Blueprint, request
from django.db import connection

from helpers.decorators import logged_in
from helpers.response import response
from helpers.endpoint import require_values

from auth.models import User, PasswordReset

roles = Blueprint("roles", __name__, url_prefix="/roles")


@roles.route("/password_reset", methods=["PATCH"])
@logged_in
def list_roles():
    pass
