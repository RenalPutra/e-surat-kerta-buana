# Generated by Django 5.1.1 on 2024-09-25 23:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0010_suketkehilangan"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SuketKelahiran",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("namab", models.CharField(max_length=255)),
                ("jenis_kelaminb", models.CharField(max_length=255)),
                ("tanggal_lahirb", models.CharField(max_length=255)),
                ("tempat_lahirb", models.CharField(max_length=255)),
                ("agamab", models.CharField(max_length=255)),
                ("alamatb", models.CharField(max_length=255)),
                ("anakke", models.CharField(max_length=255)),
                ("namaa", models.CharField(max_length=255)),
                ("umura", models.CharField(max_length=255)),
                ("pekerjaana", models.CharField(max_length=255)),
                ("alamata", models.CharField(max_length=255)),
                ("namai", models.CharField(max_length=255)),
                ("umuri", models.CharField(max_length=255)),
                ("pekerjaani", models.CharField(max_length=255)),
                ("alamati", models.CharField(max_length=255)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                ("status", models.BooleanField(blank=True, null=True)),
                ("kkb", models.URLField(blank=True, null=True)),
                ("scanfcbnb", models.URLField(blank=True, null=True)),
                ("scanfcktportub", models.URLField(blank=True, null=True)),
                ("scanfcktpsaksib1", models.URLField(blank=True, null=True)),
                ("scanfcktpsaksib2", models.URLField(blank=True, null=True)),
                ("kkd", models.URLField(blank=True, null=True)),
                ("kk_ktportud", models.URLField(blank=True, null=True)),
                ("scanfcktpsaksid1", models.URLField(blank=True, null=True)),
                ("scanfcktpsaksid2", models.URLField(blank=True, null=True)),
                (
                    "penulis",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
