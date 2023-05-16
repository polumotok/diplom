# Generated by Django 4.2 on 2023-05-15 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_orders', '0004_alter_orders_paymenttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='id',
            new_name='orderId',
        ),
        migrations.AlterField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app_orders.orders'),
        ),
    ]
