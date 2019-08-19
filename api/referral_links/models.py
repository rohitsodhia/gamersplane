# class ReferralLink:

#     def __init__(self, **props):
#         fields = ['key', 'title', 'link', 'order']
#         for field in fields:
#             setattr(self, field, props.get(field, None))

from djmodels.db import models


class ReferralLink(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255, default=None)
    link = models.CharField(max_length=255, default=None)
    order = models.IntegerField()

    class Meta:
        db_table = "referral_links"