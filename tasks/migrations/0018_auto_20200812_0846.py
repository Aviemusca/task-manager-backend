# Generated by Django 3.0.8 on 2020-08-12 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20200812_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 8, 46, 34, 597638)),
        ),
    ]
