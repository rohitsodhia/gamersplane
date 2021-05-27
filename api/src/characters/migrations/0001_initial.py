# Generated by Django 3.1.7 on 2021-04-24 20:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("systems", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deletedAt", models.DateTimeField(null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("label", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="system",
                        to="systems.system",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("pc", "PC"), ("npc", "NPC")],
                        max_length=5,
                    ),
                ),
                ("data", models.JSONField(null=True)),
            ],
            options={
                "db_table": "characters",
            },
        ),
    ]
