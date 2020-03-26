from django.db.models import Model, CharField, BooleanField, DateTimeField, Manager
from django_mysql.models import JSONField


class System(Model):
    class Meta:
        db_table = "systems"

    id = CharField(max_length=20, primary_key=True)
    name = CharField(max_length=40)
    sortName = CharField(max_length=40)
    publisher = JSONField(null=True)
    generes = JSONField(null=True)
    basics = JSONField(null=True)
    hasCharSheet = BooleanField(default=True)
    enabled = BooleanField(default=True)
    createdOn = DateTimeField(auto_now_add=True)
    updatedOn = DateTimeField(auto_now=True)

    objects = EnabledSystemsManager()
    all_objects = Manager()


class EnabledSystemsManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(enabled=True)
