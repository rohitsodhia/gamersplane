import json
from flask import Blueprint, jsonify, request

from database import db

from auth.models import User

auth = Blueprint("auth", __name__)


@auth.route("/auth/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
    except KeyError:
        return jsonify({"errors": [{"id": "no_email"}]})
    dbc = db.cursor()
    dbc.execute("SELECT * FROM users WHERE email = %(email)s", {"email": email})
    if dbc.rowcount:
        user = User(**dbc.fetchone())
        try:
            password = request.json["password"]
        except KeyError:
            return jsonify({"errors": [{"id": "no_password"}]})
        if user.check_pass(password):
            return jsonify({"data": {"logged_in": True, "jwt": user.generate_jwt()}})
    return jsonify({"errors": [{"id": "invalid_user"}]})
