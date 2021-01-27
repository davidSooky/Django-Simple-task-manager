from django.contrib.auth.models import User
from django.db.models.signals import post_save
from task_app.models import Engineer

def engineer_profile(sender, instance, created, **kwargs):
    if created:
        Engineer.objects.create(owner=instance, email=instance.email, first_name = instance.first_name, last_name=instance.last_name)

post_save.connect(engineer_profile, sender=User)
