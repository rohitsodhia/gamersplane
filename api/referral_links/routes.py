from flask import Blueprint, jsonify

referral_links = Blueprint('referral_links', __name__)


@referral_links.route('/referral_links', methods=['GET'])
def get_referral_links():
    return jsonify({'test': 'asdf'})
