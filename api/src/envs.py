import os

ENVIRONMENT = os.getenv("FLASK_ENV", "dev")

SERVER_NAME = os.getenv("SERVER_NAME")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_TTL = os.getenv("REDIS_TTL")

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

EMAIL_URI = os.getenv("EMAIL_URI")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_LOGIN = os.getenv("EMAIL_LOGIN")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
