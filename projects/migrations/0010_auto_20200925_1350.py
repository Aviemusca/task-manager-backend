# Generated by Django 3.0.8 on 2020-09-25 13:50

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200925_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 13, 50, 5, 170554)),
        ),
    ]
