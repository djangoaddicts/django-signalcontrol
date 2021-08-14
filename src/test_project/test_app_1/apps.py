from django.apps import AppConfig


class TestApp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_app_1'
    verbose_name = "test application for signalcontrol"

    def ready(self):
        import test_app_1.signals
