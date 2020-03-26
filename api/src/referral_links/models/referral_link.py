from django.db import models


class ReferralLink(models.Model):
    class Meta:
        db_table = "referral_links"

    key = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)
    enabled = models.BooleanField(default=True)
