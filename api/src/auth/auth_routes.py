from flask import Blueprint, request

from helpers.response import response
from helpers.endpoint import require_values
from helpers.email import get_template, send_email

from auth.models import User
from auth import functions
from tokens.models import AccountActivationToken, PasswordResetToken

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

    new_user = User(email=email, username=username)
    new_user.set_password(password)
    errors = functions.check_for_existing_user(new_user)
    if errors:
        return response.errors({"errors": errors})

    functions.register_user(new_user)

    return response.success()


@auth.route("/activate/<token>", methods=["POST"])
def activate_user(token):
    try:
        account_activation_token = AccountActivationToken.objects.get(token=token)
    except AccountActivationToken.DoesNotExist:
        return response.errors({"invalid_token": True})

    user = account_activation_token.user
    user.activate()
    account_activation_token.use()
    return response.success()


@auth.route("/password_reset", methods=["POST"])
def generate_password_reset():
    fields_missing = require_values(request.json, ["email"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    email = request.json["email"]
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return response.errors({"no_account": True})

    try:
        password_reset = PasswordResetToken.objects.get(user=user)
    except PasswordResetToken.DoesNotExist:
        password_reset = PasswordResetToken(user=user)
        password_reset.save()
    email_content = get_template(
        "auth/templates/reset_password.html",
        reset_link="http://gamersplane.com/auth/resetPass/" + password_reset.token,
    )
    send_email(email, "Password reset for Gamers' Plane", email_content)

    return response.success()


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
