# Generated by Django 3.1.5 on 2021-08-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Update Date")),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("picture", models.URLField(verbose_name="Picture")),
            ],
            options={
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
            },
        ),
    ]
