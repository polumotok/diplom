from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.FloatField()
    status = models.TextField(null=False, blank=True)