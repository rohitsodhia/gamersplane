if __name__ == "app":
    import django

    django.setup()


from random import seed

from flask import Flask
from flask_cors import CORS

import middleware
from authorization.routes import authorization
from users.routes import users
from referral_links.routes import referral_links
from systems.routes import systems
from permissions.roles_routes import roles
from permissions.permissions_routes import permissions
from forums.forums_routes import forums

seed()


def create_app():
    app = Flask(__name__)
    CORS(app, origins="*")

    app.before_request(middleware.initialize)
    app.before_request(middleware.validate_jwt)

    app.register_blueprint(authorization)
    app.register_blueprint(users)
    app.register_blueprint(referral_links)
    app.register_blueprint(systems)
    app.register_blueprint(roles)
    app.register_blueprint(permissions)
    app.register_blueprint(forums)

    return app
