# Generated by Django 3.0.8 on 2020-08-12 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_task_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='task_order',
        ),
    ]
