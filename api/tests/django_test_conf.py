from django_apps import apps


DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "test_gamersplane"}
}
INSTALLED_APPS = apps
SECRET_KEY = "asdf"
