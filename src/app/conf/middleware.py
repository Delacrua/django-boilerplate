from app.conf.environ import env

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if not env("DEBUG", cast=bool, default=False):
    MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")
else:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
