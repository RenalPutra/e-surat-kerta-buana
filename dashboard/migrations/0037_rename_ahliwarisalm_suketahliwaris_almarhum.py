# Generated by Django 5.1.1 on 2024-10-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0036_suketahliwaris_ahliwarisalm_suketahliwaris_istri_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="suketahliwaris",
            old_name="ahliwarisalm",
            new_name="almarhum",
        ),
    ]