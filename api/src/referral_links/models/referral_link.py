from django.db import models


class ReferralLink(models.Model):

    key = models.CharField(max_length=32, primary_key=True)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)
