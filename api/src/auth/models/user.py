import bcrypt
import datetime
import jwt

from django.db import models

from envs import JWT_ALGORITHM, JWT_SECRET_KEY


class UserManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.inactive = kwargs.pop("inactive", False)
        self.banned = kwargs.pop("banned", False)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = models.QuerySet(self.model)
        if not self.inactive:
            queryset = queryset.filter(activatedOn__isnull=False)
        if not self.banned:
            queryset = queryset.filter(banned__isnull=True)
        return queryset


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
    all_objects = UserManager(inactive=True, banned=True)

    MIN_PASSWORD_LENGTH = 8

    @staticmethod
    def validate_pass(password: str) -> list:
        invalid = []
        if len(password) < User.MIN_PASSWORD_LENGTH:
            invalid.append("pass_too_short")
        return invalid

    @staticmethod
    def hash_pass(password: str) -> str:
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    def set_password(self, password: str) -> bool:
        pass_valid = User.validate_pass(password)
        if pass_valid == []:
            self.password = self.hash_pass(password)
            return True
        return False

    def activate(self):
        self.activatedOn = datetime.datetime.utcnow()
        self.save()
        return self

    def check_pass(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def generate_jwt(self, exp_len: int = None) -> str:
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
