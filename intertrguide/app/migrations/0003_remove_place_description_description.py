# Generated by Django 5.0.6 on 2024-07-07 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_place_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='description',
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='app.place')),
            ],
        ),
    ]
