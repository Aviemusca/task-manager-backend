# Generated by Django 3.0.8 on 2020-08-11 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 18, 15, 14, 53, 920487)),
        ),
    ]