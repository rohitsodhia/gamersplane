from django.db import models
from helpers.base_models import SoftDeleteModel, SoftDeleteManager


class EnabledReferralLinksManager(SoftDeleteManager):
    def get_queryset(self):
        return super().get_queryset().filter(enabled=True)


class ReferralLink(SoftDeleteModel):
    class Meta:
        db_table = "referral_links"

    key = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)
    enabled = models.BooleanField(default=True)

    objects = EnabledReferralLinksManager()
    all_objects = models.Manager()
