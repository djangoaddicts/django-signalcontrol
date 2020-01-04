from __future__ import unicode_literals

from django.apps import AppConfig


class UserExtensionsConfig(AppConfig):
    name = 'userextensions'
    verbose_name = "User Extensions"

    def ready(self):
        import userextensions.signals
