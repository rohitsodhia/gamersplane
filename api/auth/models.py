import bcrypt, jwt, os

from model import Model


class User(Model):

    _fields = [
        "activatedOn",
        "aim",
        "avatarExt",
        "banned",
        "birthday",
        "email",
        "enableFilter",
        "games",
        "gender",
        "gmail",
        "joinDate",
        "lastActivity",
        "location",
        "newGameMail",
        "password",
        "postSide",
        "realName",
        "reference",
        "salt",
        "showAge",
        "showAvatars",
        "showTZ",
        "stream",
        "suspendedUntil",
        "timezone",
        "twitter",
        "userId",
        "username",
    ]

    def hash_pass(self, password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed

    def validate_pass(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def generate_jwt(self):
        return jwt.encode({"user_id": self.userId}, os.getenv("SECRET_KEY"), algorithm="HS256").decode("utf-8")
