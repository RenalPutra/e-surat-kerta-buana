# Generated by Django 5.1.1 on 2024-09-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_suketbelummenikah_date_suketbelummenikah_status"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SuketBelumMenikah",
        ),
    ]
