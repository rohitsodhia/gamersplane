import os

from django_apps import apps


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": "3306",
    }
}
INSTALLED_APPS = apps
