import os
import jwt

from flask import g, request

from helpers.response import response

from auth.models import User


def initialize():
    response.reset()


def validate_jwt():
    g.user = None

    jwt_token = request.headers.get("Authorization")
    if jwt_token:
        jwt_token = jwt_token[7:]
        try:
            jwt_body = jwt.decode(
                jwt_token,
                os.getenv("JWT_SECRET_KEY"),
                algorithm=os.getenv("JWT_ALGORITHM"),
            )
        except jwt.ExpiredSignatureError:
            return

        user = User.objects.get(id=jwt_body["user_id"])
        g.user = user
