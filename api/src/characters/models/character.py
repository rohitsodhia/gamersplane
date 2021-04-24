from django.db import models
from helpers.base_models import SoftDeleteModel


class Character(SoftDeleteModel):
    class Meta:
        db_table = "characters"

    class Statuses(models.Choices):
        OPEN = True, "Open"
        CLOSED = False, "Closed"

    name = models.TextField(max_length=100)
