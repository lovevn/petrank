import os
import binascii

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = binascii.hexlify(os.urandom(24)).decode()

VERSION = "0.1.0"

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
 "core",
 "pets"
]

MIDDLEWARE = [
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../static"))

TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
 "OPTIONS": {
  "context_processors": [
   "django.template.context_processors.request"
  ],
 },
}]
