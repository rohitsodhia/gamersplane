from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class RolePermission(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "role_permissions"

    role = models.ForeignKey(
        "permissions.Role", db_column="roleId", on_delete=models.PROTECT
    )
    permission = models.ForeignKey(
        "permissions.Permission", db_column="permissionId", on_delete=models.PROTECT
    )
