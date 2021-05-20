from rest_framework import serializers

from forums.models import Forum
from helpers.cache import CacheKeys, get_objects_by_id


class ParentForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            "id",
            "title",
        ]


class ChildForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            "id",
            "title",
            "description",
            "order",
            "threadCount",
        ]


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"

    parent = ParentForumSerializer()
    children = serializers.ListField(child=ChildForumSerializer(), allow_empty=True)
    heritage = serializers.SerializerMethodField()

    def get_heritage(self, obj):
        forum_ids = [1] + obj.heritage
        forums: list[Forum] = get_objects_by_id(
            forum_ids, Forum, CacheKeys.FORUM_DETAILS.value
        )
        serialized_forums = [ParentForumSerializer(forums[id]).data for id in forum_ids]
        return serialized_forums
