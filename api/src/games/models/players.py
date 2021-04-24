from django.db import models

from helpers.base_models import SoftDeleteModel, TimestampedModel


class Player(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "players"

    class States(models.TextChoices):
        APPLIED = "applied", "Applied"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        REMOVED = "removed", "Removed"
        LEFT = "left", "Left"

    game = models.ForeignKey("games.Game", db_column="gameId", on_delete=models.PROTECT)
    user = models.ForeignKey("users.User", db_column="userId", on_delete=models.PROTECT)
    state = models.CharField(max_length=8, choices=States.choices)
