# Generated by Django 5.1.1 on 2024-10-08 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0031_skck_persyaratan_suketktpbedanama_berkas1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="suketmtq",
            name="dusun",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketmtq",
            name="keperluan",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketmtq",
            name="tahunmenetap",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]