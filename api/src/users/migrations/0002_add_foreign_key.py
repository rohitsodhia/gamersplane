# Generated by Django 3.1 on 2021-02-16 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("users", "0001_initial"), ("roles", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="RoleMembership",
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
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="roles.role"
                    ),
                ),
                ("deletedAt", models.DateTimeField(null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
            ],
            options={"db_table": "roleMembership"},
        ),
        migrations.AddField(
            model_name="user",
            name="roles",
            field=models.ManyToManyField(
                related_name="users", through="users.RoleMembership", to="roles.Role"
            ),
        ),
        migrations.AddField(
            model_name="rolemembership",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="users.user"
            ),
        ),
    ]