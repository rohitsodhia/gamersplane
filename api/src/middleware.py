import os
import jwt

from flask import g, request

from helpers.response import response

from users.models import User


def initialize():
    response.reset()


def validate_jwt():
    g.user = None

    token = request.headers.get("Authorization")
    if token[:7] != "Bearer ":
        return
    if token:
        token = token[7:]
        try:
            jwt_body = jwt.decode(
                token,
                os.getenv("JWT_SECRET_KEY"),
                algorithms=os.getenv("JWT_ALGORITHM"),
            )
        except jwt.ExpiredSignatureError:
            return

        try:
            user = User.objects.get(id=jwt_body["user_id"])
        except User.DoesNotExist:
            return
        g.user = user
