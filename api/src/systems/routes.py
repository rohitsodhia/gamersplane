from flask import Blueprint, request

from helpers.response import response
from systems.models import System

systems = Blueprint("systems", __name__, url_prefix="/systems")


@systems.route("/", methods=["GET"])
def get_systems():
    systems = System.objects
    if request.values.get("basic"):
        systems = systems.basic()
    systems = systems.order_by("sortName").values()

    return response.success({"systems": [system for system in systems]})
