if __name__ == "app":
    import django

    django.setup()


from random import seed

from flask import Flask, jsonify
from flask_cors import CORS

import middleware
from referral_links.routes import referral_links
from systems.routes import systems
from auth.auth_routes import auth
from auth.roles_routes import roles

seed()

app = Flask(__name__)
CORS(app, origins="*")

app.before_request(middleware.initialize)
app.before_request(middleware.validate_jwt)

app.register_blueprint(referral_links)
app.register_blueprint(systems)
app.register_blueprint(auth)
app.register_blueprint(roles)

if __name__ == "__main__":
    app.run()
