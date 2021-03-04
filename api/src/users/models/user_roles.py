from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class UserRoles(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "user_roles"

    user = models.ForeignKey("users.User", db_column="userId", on_delete=models.PROTECT)
    role = models.ForeignKey(
        "permissions.Role", db_column="roleId", on_delete=models.PROTECT
    )
