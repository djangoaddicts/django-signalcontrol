from __future__ import unicode_literals

from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'userprofile'
    verbose_name = "User Profile"

    def ready(self):
        import userprofile.signals
