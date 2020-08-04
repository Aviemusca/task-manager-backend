# Generated by Django 3.0.8 on 2020-08-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[
                    (1, "low"),
                    (2, "below medium"),
                    (3, "medium"),
                    (4, "above medium"),
                    (5, "high"),
                ],
                default=3,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="state",
            field=models.IntegerField(
                choices=[
                    ("0", "no progress"),
                    ("1", "in progress"),
                    ("2", "completed"),
                ],
                default="0",
            ),
        ),
    ]
