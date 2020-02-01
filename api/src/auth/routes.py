import json

from flask import Blueprint, jsonify, request
from django.db import connection

from auth.models import User

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
    errors = {}
    fields_missing = []

    email = request.json.get("email")
    if not email:
        fields_missing.append("email")

    username = request.json.get("username")
    if not username:
        fields_missing.append("username")

    password = request.json.get("password")
    if not password:
        fields_missing.append("password")
    else:
        pass_valid = User.validate_pass(password)
        if pass_valid is not True:
            errors[f"pass_{pass_valid}"] = True

    if len(fields_missing):
        errors["fields_missing"] = fields_missing
    if len(errors):
        return jsonify({"errors": errors})

    with connection.cursor() as dbc:
        dbc.execute(
            "SELECT email, username FROM users WHERE email = %(email)s OR username = %(username)s",
            {"email": email, "username": username},
        )
        if dbc.rowcount:
            errors = {}
            for reg_email, reg_username in dbc:
                if reg_email == email:
                    errors["email_taken"] = True
                if reg_username == username:
                    errors["username_taken"] = True
            if len(errors):
                return jsonify({"errors": errors})

        new_user = User(email=email, username=username, password=password)
        new_user.save()
        new_user.send_activation_email()

        return jsonify({"success": True})
