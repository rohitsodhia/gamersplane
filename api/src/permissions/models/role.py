from django.db import models
from helpers.functions import pluralize
from helpers.base_models import TimestampedModel, SoftDeleteModel


class Role(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "roles"

    name = models.CharField(max_length=64, unique=True)
    plural = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(
        "users.User", db_column="userId", on_delete=models.PROTECT
    )
    permissions = models.ManyToManyField(
        "permissions.Permission",
        related_name="roles",
        through="permissions.RolePermission",
    )

    def save(self):
        if not self.plural:
            self.plural = pluralize(self.name)

        super().save()
