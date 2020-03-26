from django.db import models
from django_mysql.models import JSONField


class EnabledSystemsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(enabled=True)

    def basic(self):
        return self.get_queryset().only("id", "name", "sortName")


class System(models.Model):
    class Meta:
        db_table = "systems"

    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=40)
    sortName = models.CharField(max_length=40)
    publisher = JSONField(null=True)
    generes = JSONField(null=True)
    basics = JSONField(null=True)
    hasCharSheet = models.BooleanField(default=True)
    enabled = models.BooleanField(default=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    objects = EnabledSystemsManager()
    all_objects = models.Manager()
