from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        ordering = ['title']
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(max_length=100, null=True)
    href = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.title



class Subcategory(models.Model):
    class Meta:
        verbose_name = 'Subcategory'
        ordering = ['title']
    title = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, upload_to='Subcategory/')
    subcategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    href = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

def product_images_directory_path(instance:"ProductImage", filename:str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )
class Product(models.Model):
    class Meta:
        verbose_name_plural = ('products')
        verbose_name = ('products')
        ordering = ['title']
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='category')
    description = models.TextField(null=False, blank=True)
    fullDescription = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1, verbose_name=("цена"))
    count = models.DecimalField(default=0, max_digits=5, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)
    href = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    preview = models.ImageField(null=True, blank=True, upload_to=product_images_directory_path)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_images_directory_path)

    def __str__(self):
        return self.image.url

class tags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class specifications(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    count = models.DecimalField(default=1, max_digits=12, decimal_places=2, verbose_name=('count'))