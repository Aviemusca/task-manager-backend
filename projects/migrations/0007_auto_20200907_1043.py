# Generated by Django 3.0.8 on 2020-09-07 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20200901_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 14, 10, 42, 58, 469195)),
        ),
    ]
