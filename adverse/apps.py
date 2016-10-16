from django.apps import AppConfig


class AdverseConfig(AppConfig):
    name = 'adverse'

    def ready(self):
        import adverse.signals # register receiver functions for signals
