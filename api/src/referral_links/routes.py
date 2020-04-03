from flask import Blueprint

from helpers.response import response

from referral_links.models import ReferralLink

referral_links = Blueprint("referral_links", __name__)


@referral_links.route("/referral_links", methods=["GET"])
def get_referral_links():
    links = ReferralLink.objects.order_by("order").values()
    return response.success({"referralLinks": [link for link in links]})
