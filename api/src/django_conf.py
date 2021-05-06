import envs
from django_apps import apps


def make_key(key, key_prefix, version):
    return key


SECRET_KEY = envs.DJANGO_SECRET_KEY
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": envs.MYSQL_DATABASE,
        "USER": envs.MYSQL_USER,
        "PASSWORD": envs.MYSQL_PASSWORD,
        "HOST": envs.MYSQL_HOST,
        "PORT": "3306",
    }
}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": envs.REDIS_HOST,
        "TIMEOUT": envs.REDIS_TTL,
        "OPTIONS": {
            "MAX_ENTRIES": 1000000,
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        "KEY_FUNCTION": make_key,
    }
}
INSTALLED_APPS = apps
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
