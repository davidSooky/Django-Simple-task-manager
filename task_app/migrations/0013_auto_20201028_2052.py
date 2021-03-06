# Generated by Django 3.1 on 2020-10-28 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_app', '0012_auto_20201028_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='follower_id',
        ),
        migrations.RemoveField(
            model_name='engineer',
            name='following_id',
        ),
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
