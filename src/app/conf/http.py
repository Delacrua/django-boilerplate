from app.conf.environ import env

ALLOWED_HOSTS = ["*"]


if env("DEBUG", cast=bool, default=False):
    INTERNAL_IPS = ["127.0.0.1"]
