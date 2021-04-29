from rest_framework import serializers

from forums.models import Forum
from forums.models.forum import get_forums_by_id


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
        forum_ids = [1] + [int(id) for id in obj.heritage.split("-")]
        forums = get_forums_by_id(forum_ids)
        serialized_forums = [ParentForumSerializer(forums[id]).data for id in forum_ids]
        return serialized_forums
