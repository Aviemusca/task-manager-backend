# Generated by Django 3.0.8 on 2020-08-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0009_auto_20200803_1318"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[
                    (0, "low"),
                    (1, "below medium"),
                    (2, "medium"),
                    (3, "above medium"),
                    (4, "high"),
                ],
                default=2,
            ),
        ),
    ]
