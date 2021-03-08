from flask import Blueprint, request

from helpers.response import response
from helpers.endpoint import require_values
from helpers.email import get_template, send_email

from users.models import User
from users import functions as users_functions
from users.exceptions import UserExists
from tokens.models import AccountActivationToken, PasswordResetToken

authorization = Blueprint("authorization", __name__, url_prefix="/auth")


@authorization.route("/login", methods=["POST"])
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
            return response.success(
                {"logged_in": True, "jwt": user.generate_jwt(), "user": user.to_dict()}
            )
    return response.errors({"invalid_user": True})


@authorization.route("/register", methods=["POST"])
def register():
    errors = {}

    fields_missing = require_values(request.json, ["email", "username", "password"])
    if len(fields_missing):
        errors["fields_missing"] = fields_missing

    email = request.json["email"]
    username = request.json["username"]
    password = request.json["password"]
    if password:
        pass_invalid = User.validate_password(password)
        if len(pass_invalid):
            errors["pass_errors"] = pass_invalid

    if len(errors):
        return response.errors(errors)

    try:
        users_functions.register_user(email=email, username=username, password=password)
    except UserExists as e:
        response.errors(e.errors)

    return response.success()


@authorization.route("/activate/<token>", methods=["POST"])
def activate_user(token):
    try:
        account_activation_token = AccountActivationToken.objects.get(token=token)
    except AccountActivationToken.DoesNotExist:
        return response.errors({"invalid_token": True})

    user = account_activation_token.user
    user.activate()
    account_activation_token.use()
    return response.success()


@authorization.route("/password_reset", methods=["POST"])
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
        "authorization/templates/reset_password.html",
        reset_link="http://gamersplane.com/auth/resetPass/" + password_reset.token,
    )
    send_email(email, "Password reset for Gamers' Plane", email_content)

    return response.success()


@authorization.route("/password_reset", methods=["GET"])
def check_password_reset():
    fields_missing = require_values(request.args, ["email", "token"])
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    valid_token = PasswordResetToken.validate_token(
        token=request.args.get("token"), email=request.args.get("email")
    )
    return response.success({"valid_token": valid_token})


@authorization.route("/password_reset", methods=["PATCH"])
def reset_password():
    fields_missing = require_values(
        request.json, ["email", "token", "password", "confirm_password"]
    )
    if len(fields_missing):
        return response.errors({"fields_missing": fields_missing})

    password_reset = PasswordResetToken.validate_token(
        token=request.json.get("token"), email=request.json.get("email"), get_obj=True
    )
    if not password_reset:
        return response.errors({"invalid_token": True})

    errors = {}
    password, confirm_password = (
        request.json["password"],
        request.json["confirm_password"],
    )
    if password != confirm_password:
        errors["password_mismatch"] = True
    pass_invalid = User.validate_password(password)
    if len(pass_invalid):
        errors["pass_errors"] = pass_invalid

    if errors:
        return response.errors(errors)

    user = password_reset.user
    user.set_password(password)
    user.save()
    password_reset.use()

    return response.success({})
