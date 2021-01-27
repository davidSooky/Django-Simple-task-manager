from django.apps import AppConfig


class TaskAppConfig(AppConfig):
    name = 'task_app'

    def ready(self):
        import task_app.signals
