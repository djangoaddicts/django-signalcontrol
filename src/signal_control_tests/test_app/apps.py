from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = 'test_app'

    verbose_name = "test application for signalcontrol"

    def ready(self):
        import test_app.signals
