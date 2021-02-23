from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class SitePermissions(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "site_permissions"

    permission = models.CharField(max_length=64)
