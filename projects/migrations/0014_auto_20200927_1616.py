# Generated by Django 3.0.8 on 2020-09-27 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200927_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 16, 16, 41, 4578)),
        ),
    ]
