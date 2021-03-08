from datetime import datetime
from typing import Union
from uuid import uuid1 as uuid

from django.db import models


class TokenQuerySet(models.QuerySet):
    def use(self):
        return super().update(used=datetime.utcnow())

    def available(self):
        return super().filter(used=None)


class TokenManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.available = kwargs.pop("available", True)
        self.token_type = kwargs.pop("token_type", None)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = TokenQuerySet(self.model)
        if self.token_type:
            queryset = queryset.filter(token_type=self.token_type)
        if self.available:
            queryset = queryset.available()
        return queryset


def generate_token():
    return str(uuid())


class Token(models.Model):
    class Meta:
        db_table = "tokens"
        indexes = [models.Index(fields=["token"])]

    model_token_type = None

    class TokenTypes(models.TextChoices):
        ACCOUNT_ACTIVATION = "aa", "Account Activation"
        PASSWORD_RESET = "pr", "Password Reset"

    user = models.ForeignKey("users.User", db_column="userId", on_delete=models.PROTECT)
    token_type = models.CharField(max_length=2, choices=TokenTypes.choices)
    token = models.CharField(max_length=36, default=generate_token)
    requestedOn = models.DateTimeField(auto_now_add=True)
    used = models.DateTimeField(null=True, default=None)

    objects = TokenManager(token_type=model_token_type)
    all_objects = TokenManager(token_type=model_token_type, available=False)

    def save(self, *args, **kwargs):
        if self.model_token_type:
            self.token_type = self.model_token_type
        super().save(*args, **kwargs)

    @staticmethod
    def validate_token(
        token: str, email: str = None, get_obj: bool = False
    ) -> Union[bool, object]:
        token = Token.objects.filter(token=token)
        if email:
            token = token.filter(user__email=email)

        if get_obj:
            return token[0] if token else None
        return True if token else False

    def use(self):
        self.used = datetime.utcnow()
        self.save()
        return self
