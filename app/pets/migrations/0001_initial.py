# Generated by Django 5.1.7 on 2025-03-19 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LostPet",
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
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(0, "Lost"), (1, "Found")], default=0
                    ),
                ),
                (
                    "name",
                    models.CharField(default="Unknown", max_length=100, null=True),
                ),
                (
                    "species",
                    models.SmallIntegerField(
                        choices=[(0, "Other"), (1, "Dog"), (2, "Cat"), (3, "Bird")],
                        default=0,
                    ),
                ),
                ("predominant_color", models.CharField(max_length=50, null=True)),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(0, "Unknown"), (1, "Male"), (2, "Female")], default=0
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(editable=False, null=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="created_pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="pets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LastSeen",
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
                ("description", models.TextField(null=True)),
                ("location", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=64)),
                ("city", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(editable=False, null=True)),
                (
                    "pet",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="last_seen",
                        to="pets.lostpet",
                    ),
                ),
            ],
        ),
    ]
