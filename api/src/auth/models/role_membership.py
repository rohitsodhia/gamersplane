from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class RoleMembership(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "roleMembership"

    user = models.ForeignKey("auth.User", on_delete=models.PROTECT)
    role = models.ForeignKey("auth.Role", on_delete=models.PROTECT)
