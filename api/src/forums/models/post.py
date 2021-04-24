from django.db import models

from helpers.base_models import SoftDeleteModel, TimestampedModel


class Post(SoftDeleteModel, TimestampedModel):
    class Meta:
        db_table = "posts"

    class States(models.TextChoices):
        DRAFT = "d", "Draft"
        POST = "p", "Post"
        REVISION = "r", "Revision"

    thread = models.ForeignKey(
        "forums.Thread", on_delete=models.PROTECT, db_column="threadId"
    )
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, db_column="authorId"
    )
    body = models.TextField()
    state = models.CharField(max_length=1, choices=States.choices, default=States.DRAFT)
    revisionOf = models.ForeignKey("forums.Post", on_delete=models.PROTECT, null=True)
    postedAs = models.ForeignKey(
        "characters.Character", on_delete=models.PROTECT, null=True
    )
