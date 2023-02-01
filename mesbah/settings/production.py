import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from mesbah.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env_setting('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = env_setting("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = env_setting("CSRF_TRUSTED_ORIGINS").split(",")

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env_setting('DB_NAME'),
        'USER': env_setting('DB_USER'),
        'PASSWORD': env_setting('DB_PASSWORD'),
        'HOST': env_setting('DB_HOST'),
        'PORT': env_setting('DB_PORT'),
    }
}

# Sentry settings

SENTRY_DSN = env_setting('SENTRY_DSN')
SENTRY_PORT = env_setting('SENTRY_PORT')
sentry_sdk.init(
    dsn="https://{sentry_dsn}@sentry.hamravesh.com/{sentry_port}".format(
        sentry_dsn=SENTRY_DSN, sentry_port=SENTRY_PORT
    ),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
