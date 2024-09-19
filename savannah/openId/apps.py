from django.apps import AppConfig

class OpenidConfig(AppConfig):
    name = 'openId'

    def ready(self):
        import openId.signals
