# Generated by Django 4.2 on 2023-05-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_orders", "0005_rename_created_at_orders_createdat_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                    "number",
                    models.DecimalField(decimal_places=0, default=0, max_digits=8),
                ),
                ("name", models.CharField(default="card", max_length=100)),
                (
                    "month",
                    models.DecimalField(decimal_places=0, default=0, max_digits=2),
                ),
                (
                    "year",
                    models.DecimalField(decimal_places=0, default=0, max_digits=4),
                ),
                (
                    "code",
                    models.DecimalField(decimal_places=0, default=0, max_digits=3),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="orders",
            name="deliveryType",
            field=models.CharField(default="ordinary", max_length=100),
        ),
    ]
