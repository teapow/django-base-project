"""Travis-specific settings."""

from . import *

SECRET_KEY = "SECRET_KEY_NOT_IMPORTANT_WITHIN_TRAVIS"

INSTALLED_APPS.extend([
    "django_extensions",
])
