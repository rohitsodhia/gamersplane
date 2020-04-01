from flask import Blueprint, jsonify, request

from helpers.response import response
from systems.models import System

systems = Blueprint("systems", __name__)


@systems.route("/systems", methods=["GET"])
def get_systems():
    systems = System.objects
    if request.values.get("basic"):
        systems = systems.basic()
    systems = systems.order_by("sortName").values()

    return response.success({"data": {"systems": [system for system in systems]}})
