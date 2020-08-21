from datetime import datetime
from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deletedAt=datetime.utcnow())

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(deletedAt=None)

    def dead(self):
        return self.exclude(deletedAt=None)


class SoftDeleteManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop("alive_only", True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeleteQuerySet(self.model).alive()
        return SoftDeleteQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeleteModel(models.Model):
    class Meta:
        abstract = True

    deletedAt = models.DateTimeField(null=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager(alive_only=False)

    def delete(self):
        self.deletedAt = datetime.utcnow()
        self.save()

    def hard_delete(self):
        super().delete()


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
