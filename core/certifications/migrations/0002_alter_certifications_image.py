# Generated by Django 4.2 on 2023-04-28 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("certifications", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certifications",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="certf", verbose_name="Image"
            ),
        ),
    ]