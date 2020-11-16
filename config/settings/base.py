"""
Base settings to build other settings files upon.
# put "noqa F405" in endline to ignore pre-commit flake8 check
"""
from datetime import timedelta
from pathlib import Path

import environ
from boto3.session import Session

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# app/
APPS_DIR = ROOT_DIR / "app"
env = environ.Env()

# GENERAL
# ------------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG", True)
ENV = env("ENV")
TIME_ZONE = env("TIME_ZONE")
USE_TZ = True

# Multi languages
LANGUAGE_CODE = "ja"
LANGUAGES = (
    ("ja", "Japanese"),
    ("bn", "Bangladesh"),
    ("en", "English"),
    ("id", "Indonesian"),
    ("my", "Myanmar"),
    ("pt", "Portuguese"),
    ("th", "Thai"),
    ("vi", "Vietnamese"),
    ("zh-hans", "Chinese"),
)
USE_I18N = True
USE_L10N = True
LOCALE_PATHS = [str(ROOT_DIR / "locale")]
SITE_ID = 1

# URLS
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    # "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "django_celery_beat",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "storages",  # https://github.com/jschneier/django-storages
    # "cacheops ", # https://github.com/Suor/django-cacheops
    # "rules", # https://github.com/dfunckt/django-rules
]
LOCAL_APPS = [
    "app.core",
    "app.share_resources.users",
    "app.share_resources.master_data",
    "app.share_resources.event",
    "app.site_student.student_profile",
    "app.site_company.company_profile",
    "app.site_company.manuscript",
    "app.site_company.orientation",
    "app.site_company.message",
    "app.site_admin.admin_profile",
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# DATABASES
# ------------------------------------------------------------------------------
DATABASE_ENGINE = env("MYSQL_ENGINE")

DATABASES = {
    "default": {
        "ENGINE": DATABASE_ENGINE,
        "NAME": env("MYSQL_DATABASE"),
        "USER": env("MYSQL_USER"),
        "PASSWORD": env("MYSQL_PASSWORD"),
        "HOST": env("MYSQL_HOST"),
        "PORT": env.int("MYSQL_PORT"),
        "CONN_MAX_AGE": env.int("MYSQL_CONN_MAX_AGE", default=60),
        "TIME_ZONE": TIME_ZONE,
    }
}
DATABASES["default"]["ATOMIC_REQUESTS"] = False

# CACHES
# ------------------------------------------------------------------------------
REDIS_HOST = env("REDIS_HOST")
REDIS_PORT = env.int("REDIS_PORT")
REDIS_DB = env("REDIS_DB")
REDIS_PASSWORD = env("REDIS_PASSWORD")

REDIS_URL = f"redis://{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "PASSWORD": REDIS_PASSWORD,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior https://github.com/jazzband/django-redis#memcached-exceptions-behavior
            "IGNORE_EXCEPTIONS": True,
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                )
            ],
        },
    }
}

# session saved in both database & redis
# but get only from redis
# session data in database using for backup when redis restart
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# # Cacheops
# CACHEOPS_REDIS = REDIS_URL
# CACHEOPS = {
#     "app.share_resources.users.*": {"ops": "get", "timeout": 60 * 60},
# }

# MIGRATIONS
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {
    "sites": "app.contrib.migrations.sites",
    "users": "app.contrib.migrations.users",
    "admin_profile": "app.contrib.migrations.admin_profile",
    "company_profile": "app.contrib.migrations.company_profile",
    "manuscript": "app.contrib.migrations.manuscript",
    "orientation": "app.contrib.migrations.orientation",
    "message": "app.contrib.migrations.message",
    "event": "app.contrib.migrations.event",
    "master_data": "app.contrib.migrations.master_data",
    "student_profile": "app.contrib.migrations.student_profile",
}

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    # "django.contrib.auth.backends.ModelBackend",
    # "rules.permissions.ObjectPermissionBackend",  # django-rules
    "app.core.authen_backend.AuthBackend",
]
AUTH_USER_MODEL = "users.User"
# # LOGIN_REDIRECT_URL = "/" #"users:redirect"
# # LOGIN_URL = "/login"
# student site
STUDENT_LOGIN_URL = "/2022/login"
STUDENT_LOGIN_REDIRECT_URL = "/"
# company site
COMPANY_LOGIN_URL = "/company/login"
COMPANY_LOGIN_REDIRECT_URL = "/company/manuscripts"
# admin site
ADMIN_LOGIN_URL = "/admin/login"
ADMIN_LOGIN_REDIRECT_URL = "/admin/company/list"

# PASSWORDS
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # necessary to auto reload cache in client
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.locale.LocaleMiddleware",
    "app.core.middlewares.locale.CustomLocaleMiddleware",  # multi languages enable only on student-site
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(ROOT_DIR / "templates")],
        "OPTIONS": {
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                )
            ],
            "context_processors": [
                # "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "app.utils.context_processors.settings_context",
            ],
        },
    }
]

# SECURITY
# ------------------------------------------------------------------------------
# client-side JavaScript will not be able to access the session cookie
SESSION_COOKIE_HTTPONLY = True
# client-side JavaScript will not be able to access the CSRF cookie
CSRF_COOKIE_HTTPONLY = True
# SecurityMiddleware sets the X-XSS-Protection: 1; mode=block header on all responses
SECURE_BROWSER_XSS_FILTER = True
# clickjacking.XFrameOptionsMiddleware
X_FRAME_OPTIONS = "DENY"

# Celery
# ------------------------------------------------------------------------------
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 5 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# django-rest-framework
# -------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "NON_FIELD_ERRORS_KEY": "detail",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 20,
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/users/.*$"

# JWT
# ------------------------------------------------------------------------------
JWT_AUTH = {"JWT_ALLOW_REFRESH": True}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

# STORAGES
# ------------------------------------------------------------------------------
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default=None)
AWS_S3_CUSTOM_DOMAIN = (
    env("AWS_S3_CUSTOM_DOMAIN", default=None)
    or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
)
AWS_REGION_LOG = env("AWS_REGION_LOG", default=None)

AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = None
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
}

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
STATICFILES_DIRS = (str(ROOT_DIR / "static"),)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = "app.utils.storages.StaticRootS3Boto3Storage"

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(APPS_DIR / "media")
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
DEFAULT_FILE_STORAGE = "app.utils.storages.MediaRootS3Boto3Storage"

# LOGGING
# ------------------------------------------------------------------------------
boto3_session = Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_LOG,
)
LOG_STREAM = f"DjangoInfoStream_{ENV}"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(levelname)s]\t%(asctime)s\t%(name)s\t%(module)s.%(funcName)s:%(lineno)s\t%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "cloudwatch_handler": {
            "level": "INFO",
            "class": "watchtower.CloudWatchLogHandler",
            "boto3_session": boto3_session,
            "log_group": "CloudWatch-Log-Django-App",
            "stream_name": LOG_STREAM,
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "cloudwatch": {
            "handlers": ["cloudwatch_handler"],
            "level": "DEBUG",
            "propagate": True,
        }
    },
}

# FIREBASE
# ------------------------------------------------------------------------------
DATABASE_FIREBASE_URL = env("DATABASE_FIREBASE_URL")
AUTH_FIREBASE = {
    "type": env("AUTH_FIREBASE_TYPE"),
    "project_id": env("AUTH_FIREBASE_PROJECT_ID"),
    "private_key_id": env("AUTH_FIREBASE_PRIVATE_KEY_ID"),
    "private_key": env("AUTH_FIREBASE_PRIVATE_KEY"),
    "client_email": env("AUTH_FIREBASE_CLIENT_EMAIL"),
    "client_id": env("AUTH_FIREBASE_CLIENT_ID"),
    "auth_uri": env("AUTH_FIREBASE_AUTH_URI"),
    "token_uri": env("AUTH_FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": env("AUTH_FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": env("AUTH_FIREBASE_CLIENT_X509_CERT_URL"),
}

# CONSTANTS
from app import constants as CONSTANTS  # noqa F405

# OTHER
# ------------------------------------------------------------------------------
DEFAULT_STUDENT_AVT = f"{AWS_S3_CUSTOM_DOMAIN}/uploads/avatars/defaul-avt.png"
