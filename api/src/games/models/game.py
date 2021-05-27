from django.db import models
from helpers.base_models import SoftDeleteModel, TimestampedModel


class Game(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "games"

    class Statuses(models.TextChoices):
        OPEN = True, "Open"
        CLOSED = False, "Closed"

    title = models.CharField(max_length=50)
    system = models.ForeignKey(
        "systems.System", on_delete=models.PROTECT, db_column="systemId"
    )
    allowedCharSheets = models.ManyToManyField(
        "systems.System", limit_choices_to={"hasCharSheet": True}, related_name="+"
    )
    gm = models.ForeignKey("users.User", on_delete=models.PROTECT, db_column="gmId")
    created = models.DateTimeField(auto_now=True)
    start = models.DateTimeField(auto_now=True)
    end = (models.DateTimeField(null=True),)
    postFrequency = models.CharField(max_length=4)
    numPlayers = models.SmallIntegerField()
    charsPerPlayer = models.SmallIntegerField(default=1)
    description = models.TextField(null=True)
    charGenInfo = models.TextField(null=True)
    rootForum = models.ForeignKey(
        "forums.Forum", on_delete=models.PROTECT, db_column="forumId", related_name="+"
    )
    group = models.ForeignKey(
        "permissions.Role", on_delete=models.PROTECT, db_column="groupId"
    )
    status = models.BooleanField(default=Statuses.OPEN, choices=Statuses.choices)
    public = models.BooleanField()
    retired = models.DateTimeField(null=True)
