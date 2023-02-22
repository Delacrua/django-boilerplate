# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

from app.conf.environ import env

DATABASES = {
    # read os.environ["DATABASE_URL"] and raises ImproperlyConfigured exception if not found
    "default": env.db(),
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

