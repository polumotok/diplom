# Generated by Django 4.2 on 2023-04-24 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('href', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='Subcategory/')),
                ('href', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='app_products.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('fullDescription', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='цена')),
                ('count', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='Products/')),
                ('href', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app_products.subcategory')),
            ],
            options={
                'verbose_name': 'products',
                'verbose_name_plural': 'products',
                'ordering': ['title'],
            },
        ),
    ]
