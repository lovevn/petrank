import os
import binascii

from .secrets import SECRET_KEY

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = binascii.hexlify(os.urandom(24)).decode()

VERSION = "0.3.0"

DATABASES = {"default": {
 "ENGINE": "django.db.backends.sqlite3",
 "NAME": os.path.join(BASE_DIR, "db.sqlite3")
}}

ALLOWED_HOSTS = []
DEBUG = True

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [
 "django.contrib.contenttypes",
 "django.contrib.staticfiles",
 "django.contrib.humanize",
 "django.contrib.auth",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.admin",
 "django_unused_media",
 "sass_processor",
 "track",
 "core",
 "pets"
]

MIDDLEWARE = [
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "django.contrib.messages.middleware.MessageMiddleware",
 "track.middleware.inspect_response"
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../static"))
SASS_PROCESSOR_ROOT = os.path.abspath(os.path.join(BASE_DIR, "core", "static"))
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
 "OPTIONS": {
  "context_processors": [
   "django.contrib.auth.context_processors.auth",
   "django.contrib.messages.context_processors.messages"
  ],
 },
}]

TRACK_TZ = "Europe/London"
TRACK_PATH_EXCLUDE = [r"\.ico$", r"\.txt$", r"^/admin", r"^/apple"]
GEOIP_PATH = "/usr/local/bin/geolite2"
