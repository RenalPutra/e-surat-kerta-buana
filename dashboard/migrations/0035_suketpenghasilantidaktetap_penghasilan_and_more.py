# Generated by Django 5.1.1 on 2024-10-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0034_suketkelahiran_persyaratan"),
    ]

    operations = [
        migrations.AddField(
            model_name="suketpenghasilantidaktetap",
            name="penghasilan",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketvaksinnikah",
            name="pengantar",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]