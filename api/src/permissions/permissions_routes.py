from flask import Blueprint, request

from helpers.decorators import logged_in
from helpers.response import response
from helpers.endpoint import require_values

permissions = Blueprint("permissions", __name__, url_prefix="/permissions")


@permissions.route("/", methods=["GET"])
@logged_in
def list_permissions():

    pass
