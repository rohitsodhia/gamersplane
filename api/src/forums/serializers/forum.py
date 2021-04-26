from django.db import models
from rest_framework import serializers

from forums.models import Forum


class ParentForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            "id",
            "title",
        ]


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = "__all__"

    parent = ParentForumSerializer()
