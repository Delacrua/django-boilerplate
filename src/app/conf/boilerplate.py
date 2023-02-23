from pathlib import Path

from app.conf.environ import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = "app.urls"

# Disable built-in ./manage.py test command in favor of pytest
TEST_RUNNER = "app.test.disable_test_command_runner.DisableTestCommandRunner"

WSGI_APPLICATION = "app.wsgi.application"


# If you're developing with a Django server in a Docker container with docker,
# the instructions for enabling the toolbar don't work.
# The reason is related to the fact that the actual address that you would need
# to add to INTERNAL_IPS is going to be something dynamic, # like 172.24.0.1.
# Rather than trying to dynamically set the value of INTERNAL_IPS,
# the straightforward solution is to replace the function that enables the toolbar

if env("DEBUG", cast=bool, default=False):
    DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda _request: env("DEBUG")}
