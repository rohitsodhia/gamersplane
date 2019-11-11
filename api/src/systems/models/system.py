from django.db.models import Model, CharField, BooleanField, DateTimeField
from django_mysql.models import JSONField


class System(Model):
    class Meta:
        db_table = "systems"

    id = CharField(max_length=20, primary_key=True)
    name = CharField(max_length=40)
    sortName = CharField(max_length=40)
    publisher = JSONField()
    generes = JSONField()
    basics = JSONField()
    hasCharSheet = BooleanField(default=True)
    enabled = BooleanField(default=True)
    createdOn = DateTimeField(auto_now_add=True)
    updatedOn = DateTimeField(auto_now=True)
