# Generated by Django 3.1 on 2020-10-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0004_auto_20201004_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
