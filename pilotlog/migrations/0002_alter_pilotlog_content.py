# Generated by Django 5.0.1 on 2024-01-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pilotlog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pilotlog",
            name="content",
            field=models.JSONField(blank=True, null=True),
        ),
    ]