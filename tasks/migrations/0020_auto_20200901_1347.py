# Generated by Django 3.0.8 on 2020-09-01 13:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_auto_20200831_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 8, 13, 47, 56, 927674)),
        ),
    ]
