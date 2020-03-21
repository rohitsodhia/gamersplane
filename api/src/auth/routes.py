import json

from flask import Blueprint, jsonify, request
from django.db import connection

from helpers.endpoint import require_values

from auth.models import User, PasswordReset

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

    email = request.json["email"]
    username = request.json["username"]
    password = request.json["password"]
    if password:
        pass_invalid = User.validate_pass(password)
        if len(pass_invalid):
            errors["pass_errors"] = pass_invalid

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


@auth.route("/password_reset", methods=["POST"])
def generate_password_reset():
    fields_missing = require_values(request.json, ["email"])
    if len(fields_missing):
        return jsonify({"errors": {"fields_missing": fields_missing}})

    email = request.json["email"]
    user = User.objects.get(email=email)
    if not user:
        return jsonify({"errors": {"no_account": True}})

    try:
        password_reset = PasswordReset.objects.get(user=user, used__isnull=True)
    except PasswordReset.DoesNotExist:
        password_reset = PasswordReset(user=user)
        password_reset.generate_key()
        password_reset.save()
    password_reset.email()

    return jsonify({"success": True})


@auth.route("/password_reset", methods=["GET"])
def get_password_reset():
    fields_missing = require_values(request.args, ["email", "key"])

    valid_key = PasswordReset.valid_key(
        key=request.args.get("key"), email=request.args.get("email")
    )
    return jsonify({"success": True, "data": {"valid_key": valid_key}})


@auth.route("/password_reset", methods=["PATCH"])
def reset_password():
    fields_missing = require_values(
        request.json, ["email", "key", "password", "confirm_password"]
    )
    if len(fields_missing):
        return jsonify({"errors": {"fields_missing": fields_missing}})

    password_reset = PasswordReset.valid_key(
        key=request.json.get("key"), email=request.json.get("email"), get_obj=True
    )
    if not password_reset:
        return jsonify({"errors": {"invalid_key": True}})

    errors = {}
    password, confirm_password = (
        request.json["password"],
        request.json["confirm_password"],
    )
    if password != confirm_password:
        errors["password_mismatch"] = True
    pass_invalid = User.validate_pass(password)
    if len(pass_invalid):
        errors["pass_errors"] = pass_invalid

    user = password_reset.user
    user.set_password(password)
    user.save()
    password_reset.use()
    password_reset.save()

    return jsonify({"success": True, "data": {}})
