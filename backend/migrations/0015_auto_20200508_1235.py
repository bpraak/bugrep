# Generated by Django 3.0.5 on 2020-05-08 12:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_auto_20200508_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='member_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
