# Generated by Django 3.0.5 on 2020-05-08 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_auto_20200507_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='heading',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='issue',
            name='media',
            field=models.FileField(blank=True, editable=False, null=True, upload_to='./issue_media'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='backend.Project'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='reported_user',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reported_user', to=settings.AUTH_USER_MODEL),
        ),
    ]