from django.db import models
from django.db.models.deletion import PROTECT
from helpers.base_models import TimestampedModel, SoftDeleteModel


class Character(TimestampedModel, SoftDeleteModel):
    class Meta:
        db_table = "characters"

    class Type(models.TextChoices):
        PC = "pc", "PC"
        NPC = "npc", "NPC"

    label = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    system = models.ForeignKey(
        "systems.System", on_delete=models.PROTECT, related_name="system"
    )
    type = models.CharField(max_length=5, choices=Type.choices)
    data = models.JSONField(null=True)
