from flask import Flask
from referral_links import referral_links

app = Flask(__name__)
app.register_blueprint(referral_links)

if __name__ == '__main__':
    app.run()
