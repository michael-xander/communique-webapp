from django.apps import AppConfig


class CounsellingSessionsConfig(AppConfig):
    name = 'counselling_sessions'

    def ready(self):
        import counselling_sessions.signals # register receiver functions for signals
