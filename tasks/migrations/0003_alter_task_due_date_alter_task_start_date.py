# Generated by Django 4.2.2 on 2023-06-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_task_due_date_task_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
