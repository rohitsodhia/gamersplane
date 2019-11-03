from flask import Blueprint, jsonify
from django.db import connection

referral_links = Blueprint("referral_links", __name__)


@referral_links.route("/referral_links", methods=["GET"])
def get_referral_links():
    with connection.cursor() as dbc:
        dbc.execute(
            "SELECT `key`, `title`, `link`, `order` FROM referralLinks ORDER BY `order`"
        )
        return jsonify({"data": {"referralLinks": dbc.fetchall()}})
