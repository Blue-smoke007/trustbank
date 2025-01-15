# Generated by Django 5.1.4 on 2025-01-15 18:45

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
            name="TransferDetails",
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
                ("bank_name", models.TextField(blank=True, null=True)),
                (
                    "bank_account_number",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("email", models.TextField(blank=True, null=True)),
                ("iban_number", models.TextField(blank=True, null=True)),
                ("routing_number", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("amount", models.FloatField(blank=True, null=True)),
                ("currency", models.TextField(blank=True, null=True)),
                ("transfer_fee", models.TextField(blank=True, null=True)),
                ("total_amount", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
