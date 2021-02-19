from typing import Union

from django.db import connection

from authorization.functions import send_activation_email
from users.models import User
from users.exceptions import UserExists


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


def register_user(email: str, username: str, password: str) -> User:
    new_user = User(email=email, username=username)
    new_user.set_password(password)
    errors = check_for_existing_user(new_user)
    if errors:
        raise UserExists({"errors": errors})

    new_user.save()
    send_activation_email(new_user)

    return new_user
