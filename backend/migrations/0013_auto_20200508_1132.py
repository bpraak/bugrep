# Generated by Django 3.0.5 on 2020-05-08 11:32

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_auto_20200508_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=djrichtextfield.models.RichTextField(blank=True, editable=False, null=True),
        ),
    ]
