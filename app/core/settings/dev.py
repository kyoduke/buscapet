from .base import *

INSTALLED_APPS += [
    "django_browser_reload",
    "debug_toolbar",
]

ALLOWED_HOSTS = ["*"]

MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
