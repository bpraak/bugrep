# Generated by Django 3.0.5 on 2020-06-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_auto_20200613_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name', 'last_name', 'pk']},
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(null=True, upload_to='./project_media/logo'),
        ),
        migrations.AddField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='./project_media/thumbnail'),
        ),
    ]