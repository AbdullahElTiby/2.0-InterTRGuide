# Generated by Django 5.0.7 on 2024-11-02 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_audio_name_description_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='place',
        ),
    ]