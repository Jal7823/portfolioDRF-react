# Generated by Django 4.2 on 2023-04-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("skills", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("name", models.CharField(max_length=200, verbose_name="Project")),
                (
                    "description",
                    models.TextField(max_length=500, verbose_name="Description"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="projects",
                        verbose_name="Image",
                    ),
                ),
                (
                    "github",
                    models.URLField(blank=True, null=True, verbose_name="GitHub"),
                ),
                ("link", models.URLField(blank=True, null=True, verbose_name="Link")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Creation"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now_add=True, verbose_name="Updated"),
                ),
                ("language", models.ManyToManyField(to="skills.language")),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "db_table": "Projects",
            },
        ),
    ]
