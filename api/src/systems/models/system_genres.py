from django.db import models
from helpers.base_models import TimestampedModel, SoftDeleteModel


class SystemGenre(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "system_genres"

    system = models.ForeignKey(
        "systems.System", db_column="systemId", on_delete=models.PROTECT
    )
    genre = models.ForeignKey(
        "systems.Genre", db_column="genreId", on_delete=models.PROTECT
    )
