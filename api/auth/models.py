import bcrypt, jwt, os

from database import db

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

    @staticmethod
    def validate_pass(password):
        if len(password) < 8:
            return "too_short"
        return True

    @classmethod
    def register(cls, email, username, password):
        dbc = db.cursor()
        db.execute(
            "INSERT INTO users SET email = %(email)s, username = %(username)s, password = %(password)s",
            {"email": email, "username": username, "password": cls.hash_pass(password)},
        )

    @staticmethod
    def hash_pass(password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed

    def check_pass(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def generate_jwt(self):
        return jwt.encode(
            {"user_id": self.userId}, os.getenv("SECRET_KEY"), algorithm="HS256"
        ).decode("utf-8")
