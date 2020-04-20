from django.apps import AppConfig


class ControlsConfig(AppConfig):
    name = 'local_test.controls'

    def ready(self):
        import controls.signals
