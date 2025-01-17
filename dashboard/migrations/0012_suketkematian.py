# Generated by Django 5.1.1 on 2024-09-26 08:12

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0011_suketkelahiran"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SuketKematian",
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
                ("nama", models.CharField(max_length=255)),
                ("nip", models.CharField(max_length=255)),
                ("jabatan", models.CharField(max_length=255)),
                ("nokk", models.CharField(max_length=255)),
                ("namaalm", models.CharField(max_length=255)),
                ("nikalm", models.CharField(max_length=255)),
                ("ttlalm", models.CharField(max_length=255)),
                ("agamaalm", models.CharField(max_length=255)),
                ("anakkealm", models.CharField(max_length=255)),
                ("ibualm", models.CharField(max_length=255)),
                ("ayahalm", models.CharField(max_length=255)),
                ("pekerjaanalm", models.CharField(max_length=255)),
                ("kewarganegaraanalm", models.CharField(max_length=255)),
                ("alamatalm", models.CharField(max_length=255)),
                ("tanggal_kematian", models.CharField(max_length=255)),
                ("jam_kematian", models.CharField(max_length=255)),
                ("tempat_kematian", models.CharField(max_length=255)),
                ("penyebab_kematian", models.CharField(max_length=255)),
                ("tmptmakam", models.CharField(max_length=255)),
                ("tanggal_pmkn", models.CharField(max_length=255)),
                ("jam_pmkn", models.CharField(max_length=255)),
                ("pengantarrt", models.URLField(blank=True, null=True)),
                ("scankk", models.URLField(blank=True, null=True)),
                (
                    "date",
                    models.DateTimeField(blank=True, default=django.utils.timezone.now),
                ),
                ("status", models.BooleanField(blank=True, null=True)),
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
