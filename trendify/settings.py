"""
Django settings for trendify project.

Ready for PythonAnywhere deployment with proper .env loading, static files, and optional Cloudinary support.
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

# -------------------------------
# BASE DIR
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# LOAD .ENV
# -------------------------------
load_dotenv(BASE_DIR / ".env")  # ensures environment variables are loaded in WSGI

# -------------------------------
# SECURITY
# -------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "temporary-secret-key")  # fallback for testing
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["trendify.pythonanywhere.com"]

# -------------------------------
# APPLICATIONS
# -------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'import_export',
    "base",
]

# Cloudinary optional
if os.getenv("CLOUDINARY_CLOUD_NAME") and os.getenv("CLOUDINARY_API_KEY") and os.getenv("CLOUDINARY_API_SECRET"):
    INSTALLED_APPS += [
        "cloudinary",
        "cloudinary_storage",
    ]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Whitenoise for static files
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# -------------------------------
# URLS / WSGI
# -------------------------------
ROOT_URLCONF = "trendify.urls"
WSGI_APPLICATION = "trendify.wsgi.application"

# -------------------------------
# TEMPLATES
# -------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------------
# DATABASE
# -------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        'NAME': '/tmp/db.sqlite3',
    }
}

# -------------------------------
# PASSWORD VALIDATION
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------------
# INTERNATIONALIZATION
# -------------------------------
LANGUAGE_CODE = "ar"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French")),
    ("ar", _("Arabic")),
]

LOCALE_PATHS = [BASE_DIR / "locale"]

# -------------------------------
# EMAIL (optional)
# -------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() in ("true", "1", "yes")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -------------------------------
# STATIC FILES
# -------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -------------------------------
# MEDIA FILES / CLOUDINARY (optional)
# -------------------------------
if "cloudinary" in INSTALLED_APPS:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
        "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
        "API_PROXY": "http://proxy.server:3128",
    }

# -------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
