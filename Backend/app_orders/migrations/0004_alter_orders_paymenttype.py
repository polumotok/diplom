# Generated by Django 4.2 on 2023-05-15 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0003_alter_orders_address_alter_orders_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='paymentType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]