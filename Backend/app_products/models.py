from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        ordering = ['title']
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(max_length=100, null=True)


    def __str__(self):
        return self.title



class Subcategory(models.Model):
    class Meta:
        verbose_name = 'Subcategory'
        ordering = ['title']
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=100)
    subcategory = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategories')

    def __str__(self):
        return self.title


class Product(models.Model):
    class Meta:
        verbose_name_plural = ('products')
        verbose_name = ('products')
        ordering = ['title']
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    fullDescription = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1, verbose_name=("цена"))
    count = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

