from flask import Blueprint

from helpers.response import response

from referral_links.models import ReferralLink

referral_links = Blueprint("referral_links", __name__, url_prefix="/referral_links")


@referral_links.route("/", methods=["GET"])
def get_referral_links():
    links = ReferralLink.objects.order_by("order").values()
    return response.success({"referralLinks": [link for link in links]})
