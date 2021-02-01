from typing import Union

from django.db import connection

from auth.models import User
from tokens.models import AccountActivation


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
    account_activation_token = AccountActivation(user=new_user)
    account_activation_token.save()
    new_user.send_activation_email()
