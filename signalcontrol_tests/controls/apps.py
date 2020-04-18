from django.apps import AppConfig


class ControlsConfig(AppConfig):
    name = 'controls'

    def ready(self):
        import controls.signals
