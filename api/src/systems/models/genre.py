from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel, SoftDeleteManager


class Genre(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "genres"

    genre = models.CharField(max_length=40)
