import json
from flask import Blueprint, jsonify, request

from database import db

from systems.models import System

systems = Blueprint("systems", __name__)


@systems.route("/systems", methods=["GET"])
def get_systems():
    dbc = db.cursor()
    if request.values.get("basic"):
        fields = "`id`, `name`, `sortName`"
    else:
        fields = ", ".join(f"`{}`" for field in System.get_fields())
    dbc.execute(f"SELECT {fields} FROM systems WHERE enabled = 1 ORDER BY `sortName`")
    systems = dbc.fetchall()
    for system in systems:
        for field in ["publisher", "genres", "basics"]:
            if field in system and system[field]:
                system[field] = json.loads(system[field])
    return jsonify({"data": {"systems": systems}})
