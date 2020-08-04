# Generated by Django 3.0.8 on 2020-07-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_task_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="state",
            field=models.IntegerField(
                choices=[(0, "no_progress"), (1, "in_progress"), (2, "completed")],
                default=0,
            ),
        ),
    ]