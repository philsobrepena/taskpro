# Generated by Django 4.2.2 on 2023-06-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="task",
            name="start_date",
            field=models.DateTimeField(null=True),
        ),
    ]
