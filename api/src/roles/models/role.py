from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class Role(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "roles"

    class RoleTypes(models.TextChoices):
        SITE = "s", "Site"
        FORUM = "f", "Forum"

    name = models.CharField(max_length=64)
    role_type = models.CharField(max_length=1, choices=RoleTypes.choices, null=True)
    owner = models.ForeignKey(
        "users.User", db_column="userId", on_delete=models.PROTECT
    )
