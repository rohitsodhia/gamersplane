import os

from django_apps import apps


def make_key(key, key_prefix, version):
    return key


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
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv("REDIS_HOST"),
        "TIMEOUT": os.getenv("REDIS_TTL"),
        "OPTIONS": {
            "MAX_ENTRIES": 1000000,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_FUNCTION": make_key,
    }
}
INSTALLED_APPS = apps
