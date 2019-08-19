import os

SECRET_KEY = os.getenv('SECRET_KEY')
import pdb; pdb.set_trace()
DATABASES = {
    'default': {
        'ENGINE': 'djmodels.db.backends.mysql',
        'DATABASE': os.getenv('MYSQL_DATABASE'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
        'HOST': os.getenv('MYSQL_HOST'),
        'PORT': '3306',
    }
}

INSTALLED_APPS = ['referral_links']