import bcrypt
import datetime
import hashlib
import jwt
import os

from django.db import models
from helpers.base_models import SoftDeleteModel

from envs import SERVER_NAME, JWT_ALGORITHM, JWT_SECRET_KEY
from helpers.email import get_template, send_email


class UserManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.banned = kwargs.pop("banned", False)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.banned:
            return models.QuerySet(self.model)
        return models.QuerySet(self.model).filter(banned=None)


class User(models.Model):
    class Meta:
        db_table = "users"

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
    timezone = models.CharField(max_length=20, default="GMT")
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
    banned = models.DateTimeField(null=True)

    roles = models.ManyToManyField(
        "auth.Role", related_name="users", through="auth.RoleMembership"
    )

    objects = UserManager()
    all_objects = UserManager(banned=True)

    MIN_PASSWORD_LENGTH = 8

    @staticmethod
    def validate_pass(password):
        invalid = []
        if len(password) < User.MIN_PASSWORD_LENGTH:
            invalid.append("pass_too_short")
        return invalid

    @classmethod
    def register(cls, email, username, password):
        new_user = User(email=email, username=username)
        new_user.set_password(password)
        new_user.save()
        new_user.send_activation_email()

    @staticmethod
    def hash_pass(password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def set_password(self, password):
        pass_valid = User.validate_pass(password)
        if pass_valid == []:
            self.password = self.hash_pass(password)
            return True
        return False

    def check_pass(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def get_activation_link(self):
        if not self.username or not self.joinDate:
            raise ValueError
        user_hash = hashlib.md5(
            str(self.username).encode("utf-8") + str(self.joinDate).encode("utf-8")
        )
        return f"{SERVER_NAME}/register/activate/{user_hash.hexdigest()}"

    def send_activation_email(self):
        email_content = get_template(
            "auth/templates/activation.html", activation_link=self.get_activation_link()
        )
        send_email(self.email, "Activate your Gamers' Plane account!", email_content)

    def generate_jwt(self, exp_len=None):
        if not exp_len:
            exp_len = {"weeks": 2}
        return jwt.encode(
            {
                "user_id": self.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(**exp_len),
            },
            JWT_SECRET_KEY,
            algorithm=JWT_ALGORITHM,
        ).decode("utf-8")
