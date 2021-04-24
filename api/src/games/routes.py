from flask import Blueprint, request

from helpers.response import response

games = Blueprint("games", __name__)


# @tools.route("/dice", methods=["GET"])
# def roll_dice():
