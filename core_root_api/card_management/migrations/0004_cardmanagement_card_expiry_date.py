# Generated by Django 5.1.4 on 2025-01-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core_root_api_card_management", "0003_alter_cardmanagement_card_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="cardmanagement",
            name="card_expiry_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
