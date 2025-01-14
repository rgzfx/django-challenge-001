# Generated by Django 3.1.5 on 2021-08-16 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Update Date")),
                ("name", models.SlugField(unique=True, verbose_name="Name")),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Update Date")),
                ("title", models.CharField(max_length=30, verbose_name="Title")),
                ("summary", models.CharField(max_length=100, verbose_name="Summary")),
                ("firstParagraph", models.CharField(max_length=100, verbose_name="First Paragraph")),
                ("body", models.CharField(max_length=100, verbose_name="Body")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="authors.author", verbose_name="Author ID"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="articles.category", verbose_name="Category ID"
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
