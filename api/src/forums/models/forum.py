from django.db import models

from helpers.base_models import SoftDeleteModel, TimestampedModel


class Forum(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "forums"
        indexes = [models.Index(fields=["parent"]), models.Index(fields=["heritage"])]

    class ForumTypes(models.TextChoices):
        FORUM = "f", "Forum"
        CATEGORY = "c", "Category"

    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    forumType = models.CharField(
        max_length=1, choices=ForumTypes.choices, default=ForumTypes.FORUM, null=True
    )
    parent = models.ForeignKey(
        "forums.Forum", on_delete=models.PROTECT, db_column="parentId", null=True
    )
    heritage = models.TextField(max_length=25, null=True)
    order = models.IntegerField()
    game = models.ForeignKey(
        "games.Game", on_delete=models.PROTECT, db_column="gameId", null=True
    )
    threadCount = models.IntegerField(default=0)
