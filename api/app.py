from flask import Flask
from flask_cors import CORS
from referral_links.routes import referral_links

app = Flask(__name__)
CORS(app, origins="*")
app.register_blueprint(referral_links)

if __name__ == '__main__':
    app.run()
