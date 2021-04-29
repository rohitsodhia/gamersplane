from django.db import models
from django.core.cache import cache

from helpers.cache import CACHE_KEYS
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

    @property
    def children(self):
        children_objs = Forum.objects.filter(parent=self.id).order_by("order")
        children = [obj for obj in children_objs]
        return children


def get_forums_by_id(forum_ids):
    if type(forum_ids) in [int, str]:
        forum = cache.get(CACHE_KEYS["forum_details"].format(forum_id=forum_ids))
        if not forum:
            forum = Forum.objects.get(id=forum_ids)
        cache.set(CACHE_KEYS["forum_details"].format(forum_id=forum_ids), forum)
        return forum

    cache_keys = [
        CACHE_KEYS["forum_details"].format(forum_id=forum_id) for forum_id in forum_ids
    ]
    forum_caches = cache.get_many(cache_keys)
    forums = {val.id: val for key, val in forum_caches.items()}
    retrieved_forums = forums.keys()
    forums_to_get = list(set(forum_ids) - set(retrieved_forums))
    if forums_to_get:
        forum_objs = Forum.objects.filter(id__in=forums_to_get)
        for forum_obj in forum_objs:
            forums[forum_obj.id] = forum_obj
            forum_caches[
                CACHE_KEYS["forum_details"].format(forum_id=forum_obj.id)
            ] = forum_obj
    cache.set_many(forum_caches)
    return forums
