from flask import Blueprint, jsonify

from referral_links.models import ReferralLink

referral_links = Blueprint("referral_links", __name__)


@referral_links.route("/referral_links", methods=["GET"])
def get_referral_links():
    links = ReferralLink.objects.order_by("order").values()
    return jsonify({"data": {"referralLinks": [link for link in links]}})
