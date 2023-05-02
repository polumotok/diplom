from django.contrib.auth.models import User
from django.db import models


def product_user_directory_path(instance:"ProductImage", filename:str) -> str:
    return "products/product_{pk}/images/{filename}".format(
        pk=instance.user.pk,
        filename=filename,
    )

class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    avatar = models.ImageField(max_length=100,null=True, blank=True, upload_to=product_user_directory_path)
    balance = models.FloatField()
    status = models.TextField(null=False, blank=True)