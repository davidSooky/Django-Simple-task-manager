from django.db import models

class TaskCompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_completed=True)

class TaskNotCompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_completed=False)