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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    avatar = models.ImageField(null=False, blank=False, upload_to=product_user_directory_path)
    balance = models.FloatField(default=0)
    status = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.avatar.url
