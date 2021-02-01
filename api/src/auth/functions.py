from typing import Union

from django.db import connection

from envs import SERVER_NAME
from helpers.email import get_template, send_email
from auth.models import User
from tokens.models import AccountActivationToken


def check_for_existing_user(user: User) -> Union[object, None]:
    with connection.cursor() as dbc:
        dbc.execute(
            "SELECT email, username FROM users WHERE email = %(email)s OR username = %(username)s",
            {"email": user.email, "username": user.username},
        )
        if dbc.rowcount:
            errors = {}
            for reg_email, reg_username in dbc:
                if reg_email == user.email:
                    errors["email_taken"] = True
                if reg_username == user.username:
                    errors["username_taken"] = True
            if len(errors):
                return errors


def register_user(new_user: User) -> None:
    new_user.save()
    send_activation_email(new_user)


def get_activation_link(user: User) -> str:
    try:
        token = AccountActivationToken.objects.get(user=user)
    except AccountActivationToken.DoesNotExist:
        token = AccountActivationToken(user=user)
        token.save()

    if not user.username or not user.joinDate:
        raise ValueError

    return f"{SERVER_NAME}/register/activate/{token.token}"


def send_activation_email(user: User) -> None:
    email_content = get_template(
        "auth/templates/activation.html", activation_link=get_activation_link(user)
    )
    send_email(user.email, "Activate your Gamers' Plane account!", email_content)
