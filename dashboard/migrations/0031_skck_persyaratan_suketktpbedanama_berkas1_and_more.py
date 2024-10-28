# Generated by Django 5.1.1 on 2024-10-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0030_suketbelummenikah_persyaratan"),
    ]

    operations = [
        migrations.AddField(
            model_name="skck",
            name="persyaratan",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="berkas1",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="berkas2",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="dokumen1",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="dokumen2",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="namadokumen1",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="suketktpbedanama",
            name="namadokumen2",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="sukettidakmampu",
            name="dusun",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="sukettidakmampu",
            name="keperluan",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]