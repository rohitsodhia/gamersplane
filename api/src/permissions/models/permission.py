from django.db import models


class Permission(models.Model):
    class Meta:
        db_table = "permissions"

    permission = models.CharField(max_length=64, unique=True)
