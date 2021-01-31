from functools import wraps, partial
from typing import Callable

from flask import g

from helpers.response import response


def logged_in(func=None, *, permissions=None):
    if not func:
        return partial(logged_in, permissions=None)

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if not g.User:
            response.unauthorized()
        if permissions:
            pass
        return func(*args, **kwargs)

    return wrapper
