from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class RoleMembership(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "roleMembership"

    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    role = models.ForeignKey("roles.Role", on_delete=models.PROTECT)
