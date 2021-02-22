from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel, SoftDeleteManager


class Publisher(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "publishers"

    name = models.CharField(max_length=40)
    website = models.CharField(max_length=200, null=True)
