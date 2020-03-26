import json
from flask import Blueprint, jsonify, request
from django.db import connection

from systems.models import System

systems = Blueprint("systems", __name__)


@systems.route("/systems", methods=["GET"])
def get_systems():
    systems = System.objects
    if request.values.get("basic"):
        systems = systems.only("id", "name", "sortName")
    return jsonify({"data": {"systems": systems}})
