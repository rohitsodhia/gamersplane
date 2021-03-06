# Generated by Django 3.0.5 on 2020-04-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="System",
            fields=[
                (
                    "id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=40)),
                ("sortName", models.CharField(max_length=40)),
                ("publisher", models.JSONField(default=dict, null=True)),
                ("generes", models.JSONField(default=dict, null=True)),
                ("basics", models.JSONField(default=dict, null=True)),
                ("hasCharSheet", models.BooleanField(default=True)),
                ("enabled", models.BooleanField(default=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("deletedAt", models.DateTimeField(null=True)),
            ],
            options={"db_table": "systems"},
        )
    ]
