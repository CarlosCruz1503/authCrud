# Generated by Django 4.1.4 on 2022-12-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0002_task_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="date",
        ),
        migrations.AddField(
            model_name="task",
            name="date_for_complete",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="data_complete",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]