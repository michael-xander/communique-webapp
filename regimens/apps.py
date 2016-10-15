from django.apps import AppConfig


class RegimensConfig(AppConfig):
    name = 'regimens'

    def ready(self):
        import regimens.signals # register receiver functions for signals
