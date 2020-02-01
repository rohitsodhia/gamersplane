import os
import hashlib
import bcrypt
import jwt

from django.db import models

from envs import DOMAIN
from helpers.email import get_template, send_email


class User(models.Model):
    class Meta:
        db_table = "users"

    userID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=64)
    salt = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    joinDate = models.DateTimeField(auto_now=True)
    activatedOn = models.DateTimeField(null=True)
    lastActivity = models.DateTimeField(null=True)
    reference = models.CharField(max_length=200, null=True)
    enableFilter = models.BooleanField(default=True)
    showAvatars = models.BooleanField(default=True)
    avatarExt = models.CharField(max_length=3, null=True)
    timezone = models.CharField(max_length=20, default="Europe/London")
    showTZ = models.BooleanField(null=True)
    realName = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    birthday = models.DateField(null=True)
    showAge = models.BooleanField(null=True)
    location = models.CharField(max_length=100, null=True)
    aim = models.CharField(max_length=50, null=True)
    gmail = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)
    stream = models.CharField(max_length=50, null=True)
    games = models.CharField(max_length=200, null=True)
    newGameMail = models.BooleanField(default=True)
    postSide = models.CharField(max_length=1, default="r")
    suspendedUntil = models.DateTimeField(null=True)
    banned = models.BooleanField(default=False)

    @staticmethod
    def validate_pass(password):
        if len(password) < 8:
            return "too_short"
        return True

    @classmethod
    def register(cls, email, username, password):
        new_user = User(email=email, username=username, password=password)
        new_user.save()
        new_user.send_activation_email()

    @staticmethod
    def hash_pass(password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed

    def set_password(self, password):
        self.password = self.hash_pass(password)

    def check_pass(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def get_activation_link(self):
        user_hash = hashlib.md5(str(self.username) + str(self.joinDate))
        return f"{DOMAIN}/register/activate/{user_hash}"

    def send_activation_email(self):
        email_content = get_template(
            "auth/templates/activation.html", username=self.username
        )
        send_email(self.email, "Activate your Gamers' Plane account!", email_content)

    def generate_jwt(self):
        return jwt.encode(
            {"user_id": self.userID}, os.getenv("SECRET_KEY"), algorithm="HS256"
        ).decode("utf-8")
