# Generated by Django 4.2.3 on 2024-08-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_created_at_task_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=255),
        ),
    ]
