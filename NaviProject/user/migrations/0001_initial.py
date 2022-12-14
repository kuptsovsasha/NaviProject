# Generated by Django 4.1.1 on 2022-09-08 12:52

from django.db import migrations, models

import NaviProject.user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=128, null=True)),
                ("last_name", models.CharField(blank=True, max_length=128, null=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", NaviProject.user.models.UserManager()),
            ],
        ),
    ]
