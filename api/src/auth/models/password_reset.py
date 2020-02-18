from django.db import models

from auth.models import User


class PasswordReset(models.Model):
    class Meta:
        db_table = "password_resets"
        indexes = [models.Index(fields=["key"])]

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    requestedOn = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=16)
    used = models.BooleanField(default=False)
