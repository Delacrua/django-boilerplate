# Application definition
from app.conf.environ import env

APPS = [
    "app",
]

THIRD_PARTY_APPS = []

if env("DEBUG", cast=bool, default=False):
    THIRD_PARTY_APPS.append("debug_toolbar")

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = APPS + THIRD_PARTY_APPS + DEFAULT_APPS
