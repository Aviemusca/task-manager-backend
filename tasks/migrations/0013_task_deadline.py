# Generated by Django 3.0.8 on 2020-08-05 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0012_task_difficulty"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 12, 8, 36, 21, 482437)
            ),
        ),
    ]