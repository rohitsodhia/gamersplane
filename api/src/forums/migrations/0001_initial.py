# Generated by Django 3.1.7 on 2021-04-24 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0003_usermeta"),
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Forum",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(null=True)),
                (
                    "forumType",
                    models.CharField(
                        choices=[("f", "Forum"), ("c", "Category")],
                        default="f",
                        max_length=1,
                        null=True,
                    ),
                ),
                ("heritage", models.TextField(max_length=25, null=True)),
                ("order", models.IntegerField()),
                ("threadCount", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "forums",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50)),
                ("body", models.TextField()),
                (
                    "state",
                    models.CharField(
                        choices=[("d", "Draft"), ("p", "Post"), ("r", "Revision")],
                        default="d",
                        max_length=1,
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        db_column="authorId",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="users.user",
                    ),
                ),
                (
                    "postedAs",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="characters.character",
                    ),
                ),
                (
                    "revisionOf",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="forums.post",
                    ),
                ),
            ],
            options={
                "db_table": "posts",
            },
        ),
        migrations.CreateModel(
            name="Thread",
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
                ("sticky", models.BooleanField(default=False)),
                ("locked", models.BooleanField(default=False)),
                ("allowRolls", models.BooleanField(default=False)),
                ("allowDraws", models.BooleanField(default=False)),
                ("postCount", models.IntegerField(default=0)),
                (
                    "firstPost",
                    models.ForeignKey(
                        db_column="firstPostId",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="first_post",
                        to="forums.post",
                    ),
                ),
                (
                    "forum",
                    models.ForeignKey(
                        db_column="forumId",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="forums.forum",
                    ),
                ),
                (
                    "lastPost",
                    models.ForeignKey(
                        db_column="lastPostId",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="last_post",
                        to="forums.post",
                    ),
                ),
            ],
            options={
                "db_table": "threads",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="thread",
            field=models.ForeignKey(
                db_column="threadId",
                on_delete=django.db.models.deletion.PROTECT,
                to="forums.thread",
            ),
        ),
    ]