# Generated by Django 3.0.8 on 2020-09-25 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200907_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 13, 47, 57, 652817)),
        ),
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 13, 47, 57, 652874)),
        ),
    ]
