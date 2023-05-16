# Generated by Django 4.2 on 2023-05-15 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_remove_profile_id_alter_profile_avatar_and_more'),
        ('app_products', '0006_rename_tags_tags_name'),
        ('app_orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='deliveryType',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='paymentType',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='orders',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='totalCost',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=12, verbose_name='totalCost'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='app_user.profile'),
        ),
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='count')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_orders.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='app_products.product')),
            ],
        ),
    ]
