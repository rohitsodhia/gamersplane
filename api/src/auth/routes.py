import json

from flask import Blueprint, jsonify, request
from django.db import connection

from helpers.endpoint import require_values

from auth.models import User

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
    except KeyError:
        return jsonify({"errors": {"no_email": True}})
    with connection.cursor() as dbc:
        users = User.objects.raw(
            "SELECT * FROM users WHERE email = %(email)s", params={"email": email}
        )
        if users:
            user = users[0]
            try:
                password = request.json["password"]
            except KeyError:
                return jsonify({"errors": {"no_password": True}})
            if user.check_pass(password):
                return jsonify(
                    {"data": {"logged_in": True, "jwt": user.generate_jwt()}}
                )
        return jsonify({"errors": {"invalid_user": True}})


@auth.route("/register", methods=["POST"])
def register():
    errors = {}

    fields_missing = require_values(request.json, ["email", "username", "password"])
    if len(fields_missing):
        errors["fields_missing"] = fields_missing

    email = request.json.get("email")
    username = request.json.get("username")
    password = request.json.get("password")
    if password:
        pass_valid = User.validate_pass(password)
        if pass_valid is not True:
            errors[f"pass_{pass_valid}"] = True

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

        User.register(email=email, username=username, password=password)

        return jsonify({"success": True})
