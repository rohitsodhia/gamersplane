from flask import Blueprint, request

from helpers.response import response

characters = Blueprint("characters", __name__)


# @tools.route("/dice", methods=["GET"])
# def roll_dice():
