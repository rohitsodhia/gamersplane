from flask import Blueprint, request
from django.db import connection

from helpers.response import response
from helpers.endpoint import require_values
from helpers.email import get_template, send_email

from auth.models import User
from auth.functions import register_user
from tokens.models import Token

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    fields_missing = require_values(request.json, ["email", "password"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    email = request.json["email"]
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None
    if user:
        password = request.json["password"]
        if user.check_pass(password):
            return response.success({"logged_in": True, "jwt": user.generate_jwt()})
    return response.errors({"invalid_user": True})


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
        return response.errors(errors)

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
                return response.errors({"errors": errors})

        new_user = User(email=email, username=username)
        new_user.set_password(password)
        register_user(new_user)

        return response.success({})


@auth.route("/password_reset", methods=["POST"])
def generate_password_reset():
    fields_missing = require_values(request.json, ["email"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    email = request.json["email"]
    user = User.objects.get(email=email)
    if not user:
        return response.errors({"no_account": True})

    try:
        password_reset = Token.objects.get(
            user=user, token_type=Token.TokenTypes.PASSWORD_RESET, used__isnull=True
        )
    except Token.DoesNotExist:
        password_reset = Token(user=user)
        password_reset.generate_token()
        password_reset.save()
    email_content = get_template(
        "auth/templates/reset_password.html",
        reset_link="http://gamersplane.com/auth/resetPass/" + password_reset.token,
    )
    send_email(email, "Password reset for Gamers' Plane", email_content)

    return response.success({})


@auth.route("/password_reset", methods=["GET"])
def get_password_reset():
    fields_missing = require_values(request.args, ["email", "key"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    valid_key = PasswordReset.valid_key(
        key=request.args.get("key"), email=request.args.get("email")
    )
    return response.success({"valid_key": valid_key})


@auth.route("/password_reset", methods=["PATCH"])
def reset_password():
    fields_missing = require_values(
        request.json, ["email", "key", "password", "confirm_password"]
    )
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    password_reset = PasswordReset.valid_key(
        key=request.json.get("key"), email=request.json.get("email"), get_obj=True
    )
    if not password_reset:
        return response.errors({"invalid_key": True})

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

    if errors:
        return response.errors(errors)

    user = password_reset.user
    user.set_password(password)
    user.save()
    password_reset.use()
    password_reset.save()

    return response.success({})
