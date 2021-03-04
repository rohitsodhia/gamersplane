from functools import wraps, partial
from typing import Callable

from flask import g

from helpers.response import response


def logged_in(func=None, *, permissions=None):
    if not func:
        return partial(logged_in, permissions=None)

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if not g.user:
            response.unauthorized()
        if permissions:
            if type(permissions) == str:
                permissions = [permissions]
            if not g.user.admin and not bool(
                set(g.user.permissions) & set(permissions)
            ):
                response.forbidden()
        return func(*args, **kwargs)

    return wrapper
