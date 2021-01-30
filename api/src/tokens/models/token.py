import random
import string
from datetime import datetime

from django.db import models

from auth.models import User


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


class Token(models.Model):
    class Meta:
        db_table = "tokens"
        indexes = [models.Index(fields=["token"])]
        token_type = None

    class TokenTypes(models.TextChoices):
        ACCOUNT_ACTIVATION = "aa", "Account Activation"
        PASSWORD_RESET = "pr", "Password Reset"

    user = models.ForeignKey(User, db_column="userId", on_delete=models.PROTECT)
    token_type = models.CharField(max_length=2, choices=TokenTypes.choices)
    token = models.CharField(max_length=16)
    requestedOn = models.DateTimeField(auto_now_add=True)
    used = models.DateTimeField(null=True, default=None)

    objects = TokenManager()
    all_objects = TokenManager(available=False)

    def save(self, *args, **kwargs):
        if self.Meta.token_type:
            self.token_type = self.Meta.token_type
        super().save(*args, **kwargs)

    @staticmethod
    def validate_token(token, email=None, get_obj=False):
        token = Token.objects.filter(token=token)
        if email:
            token = token.filter(user__email=email)

        if get_obj:
            return token[0] if token else None
        return True if token else False
