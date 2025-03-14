# Generated by Django 5.0.6 on 2025-03-13 07:37

import django.db.models.deletion
import ekart.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Catagory",
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
                ("name", models.CharField(max_length=150)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=ekart.models.getFileName
                    ),
                ),
                ("description", models.TextField(max_length=500)),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0-show,1-Hidden"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=150)),
                ("vendor", models.CharField(max_length=150)),
                (
                    "product_image",
                    models.ImageField(
                        blank=True, null=True, upload_to=ekart.models.getFileName
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("original_price", models.FloatField()),
                ("selling_price", models.FloatField()),
                ("description", models.TextField(max_length=500)),
                (
                    "status",
                    models.BooleanField(default=False, help_text="0-show,1-Hidden"),
                ),
                (
                    "trending",
                    models.BooleanField(
                        default=False, help_text="0-default,1-Trending"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ekart.catagory"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Favourite",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ekart.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("product_qty", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ekart.product"
                    ),
                ),
            ],
        ),
    ]
