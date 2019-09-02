import json
from flask import Blueprint, jsonify, request

from database import db

from auth.models import User

auth = Blueprint("auth", __name__)


@auth.route("/auth/login", methods=["POST"])
def login():
    dbc = db.cursor()
    dbc.execute(
        "SELECT * FROM users WHERE email = %(email)s", {"email": "rohit@rhovisions.com"}
    )
    if dbc.rowcount:
        user = User(**dbc.fetchone())
        password = request.json["password"]
        if user.validate_pass(password):
            return jsonify({"data": {"logged_in": True, "jwt": user.generate_jwt()}})
    return jsonify({"errors": [{"id": "invalid_user"}]})
