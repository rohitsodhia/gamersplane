from rest_framework import serializers

from forums.models import Forum


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
