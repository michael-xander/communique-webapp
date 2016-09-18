from django.apps import AppConfig


class OccasionsConfig(AppConfig):
    name = 'occasions'

    def ready(self):
        import occasions.signals # register receiver functions for signals
