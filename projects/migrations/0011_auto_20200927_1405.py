# Generated by Django 3.0.8 on 2020-09-27 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200925_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 14, 5, 40, 438234)),
        ),
    ]
