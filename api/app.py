from flask import Flask
from flask_cors import CORS

import djmodels
djmodels.setup()

from referral_links.routes import referral_links
from systems.routes import systems

app = Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(referral_links)
app.register_blueprint(systems)

if __name__ == '__main__':
    app.run()
