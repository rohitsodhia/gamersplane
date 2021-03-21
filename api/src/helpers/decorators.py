from functools import wraps, partial
from typing import Callable

from flask import g

from helpers.response import response


def logged_in(func=None, *, permissions=None):
    if func is None:
        return partial(logged_in, permissions=permissions)

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        nonlocal permissions
        if not g.get("user"):
            return response.unauthorized()
        if permissions:
            if type(permissions) == str:
                permissions = [permissions]
            if not g.user.admin and not bool(
                set(g.user.permissions) & set(permissions)
            ):
                return response.forbidden()
        return func(*args, **kwargs)

    return wrapper
