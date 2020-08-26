import os

ENVIRONMENT = os.getenv("FLASK_ENV", "dev")

SERVER_NAME = os.getenv("SERVER_NAME")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
