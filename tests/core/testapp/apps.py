from django.apps import AppConfig


class TestappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tests.core.testapp"

    def ready(self):
        import tests.core.testapp.signals
