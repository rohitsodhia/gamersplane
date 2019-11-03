import json
from flask import Blueprint, jsonify, request
from django.db import connection

from systems.models import System
from systems.utils import generate_systems_sql

systems = Blueprint("systems", __name__)


@systems.route("/systems", methods=["GET"])
def get_systems():
    with connection.cursor() as dbc:
        sql = generate_systems_sql(request.values.get("basic"))
        dbc.execute(sql)
        systems = dbc.fetchall()
        for system in systems:
            for field in ["publisher", "genres", "basics"]:
                if field in system and system[field]:
                    system[field] = json.loads(system[field])
        return jsonify({"data": {"systems": systems}})
