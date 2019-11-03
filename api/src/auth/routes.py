import json
from flask import Blueprint, jsonify, request
from django.db import connection

from auth.models.User import User

auth = Blueprint("auth", __name__)


@auth.route("/auth/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
    except KeyError:
        return jsonify({"errors": [{"id": "no_email"}]})
    with connection.cursor() as dbc:
        dbc.execute("SELECT * FROM users WHERE email = %(email)s", {"email": email})
        if dbc.rowcount:
            user = User(**dbc.fetchone())
            try:
                password = request.json["password"]
            except KeyError:
                return jsonify({"errors": [{"id": "no_password"}]})
            if user.check_pass(password):
                return jsonify(
                    {"data": {"logged_in": True, "jwt": user.generate_jwt()}}
                )
        return jsonify({"errors": [{"id": "invalid_user"}]})


@auth.route("/auth/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]
    except KeyError:
        return jsonify({"errors": [{"id": "no_email"}]})
    try:
        username = request.json["username"]
    except KeyError:
        return jsonify({"errors": [{"id": "no_username"}]})
    with connection.cursor() as dbc:
        dbc.execute(
            "SELECT email, username FROM users WHERE email = %(email)s OR username = %(username)s",
            {"email": email, "username": username},
        )
        if dbc.rowcount:
            reg_email, reg_username = dbc.fetchone()
            errors = []
            if reg_email == email:
                errors.push("email_taken")
            if reg_username == username:
                errors.push("username_taken")
            return jsonify({"errors": [[{"id": error}] for error in errors]})

        password = request.json["password"]
        rep_password = request.json["rep_password"]
        if password != rep_password:
            return jsonify({"errors": [{"id": "pass_mismatch"}]})
        pass_valid = User.validate_pass(password)
        if pass_valid is not True:
            return jsonify({"errors": [{"id": pass_valid}]})
