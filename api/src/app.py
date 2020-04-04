import django_conf
from random import seed

from flask import Flask, jsonify
from flask_cors import CORS

import middleware
from referral_links.routes import referral_links
from systems.routes import systems
from auth.routes import auth

seed()

app = Flask(__name__)
CORS(app, origins="*")

app.before_request(middleware.validate_jwt)

app.register_blueprint(referral_links)
app.register_blueprint(systems)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run()
