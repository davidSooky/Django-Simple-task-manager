# Generated by Django 3.1 on 2020-10-28 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0016_auto_20201028_2106'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('owner_id', 'follower_id')},
        ),
        migrations.AlterUniqueTogether(
            name='following',
            unique_together={('owner_id', 'following_id')},
        ),
    ]
