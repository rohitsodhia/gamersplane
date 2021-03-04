from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class Role(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "roles"

    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(
        "users.User", db_column="userId", on_delete=models.PROTECT
    )
    permissions = models.ManyToManyField(
        "permissions.Permission",
        related_name="roles",
        through="permissions.RolePermission",
    )
