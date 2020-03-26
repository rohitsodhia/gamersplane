from django.db import models


class EnabledReferralLinksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(enabled=True)


class ReferralLink(models.Model):
    class Meta:
        db_table = "referral_links"

    key = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)
    enabled = models.BooleanField(default=True)

    objects = EnabledReferralLinksManager()
    all_objects = models.Manager()
