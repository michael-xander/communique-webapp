from django.apps import AppConfig


class AdmissionsConfig(AppConfig):
    name = 'admissions'

    def ready(self):
        import admissions.signals # register receiver functions for signals
