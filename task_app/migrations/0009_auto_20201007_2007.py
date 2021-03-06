# Generated by Django 3.1 on 2020-10-07 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0008_engineer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/profile.png', null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_app.engineer')),
            ],
        ),
    ]
