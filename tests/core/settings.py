"""
Minimal file so Sphinx can work with Django for autodocumenting.

Location: /docs/django_settings.py
"""
from pathlib import Path

import os
import random

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = str(random.getrandbits(32))

# INSTALLED_APPS with these apps is necessary for Sphinx to build
# without warnings & errors
# Depending on your package, the list of apps may be different
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djangoaddicts.signalcontrol",
    "tests.core.testapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tests.core.urls"

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        "TEST_NAME": "test.sqlite3",
        "USER": "signalcontrol",
        "PASSWORD": "signalcontrol",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "core", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

USE_TZ = True

STATIC_ROOT = os.path.join(str(BASE_DIR), "staticroot")
STATIC_URL = "/static/"
