"""Local development settings."""

from . import *

DEBUG = True

SECRET_KEY = "SECRET_KEY_GOES_HERE"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
