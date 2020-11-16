from .base import *  # noqa

# GENERAL
# ------------------------------------------------------------------------------
DEBUG = True
ALLOWED_HOSTS = ["*"]

# django-debug-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    "debug_toolbar",
    "widget_tweaks",
    "django_extensions",
    "django_user_agents",
]  # noqa F405
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    # "app.core.middlewares.debug_query.QueryCountDebugMiddleware",
]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

# debug toolbar is shown only if your IP address is listed in the INTERNAL_IPS
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
# in case using docker
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# minimal logging
import sys

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django.db.backends": {
            "level": "DEBUG",
        },
    },
}

del DEFAULT_FILE_STORAGE
del STATICFILES_STORAGE
