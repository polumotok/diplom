from django.db import models

from app_products.models import Product
from app_user.models import Profile


class Orders(models.Model):
    orderId = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="profile"
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    deliveryType = models.CharField(max_length=100, default="ordinary")
    paymentType = models.CharField(max_length=50, null=True)
    totalCost = models.DecimalField(
        default=0, max_digits=12, decimal_places=2, verbose_name="totalCost"
    )
    status = models.BooleanField(default=False)
    city = models.CharField(max_length=100, default=None, null=True)
    address = models.CharField(max_length=100, default=None, null=True)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class Order_product(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_orders"
    )
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    count = models.DecimalField(
        default=1, max_digits=12, decimal_places=2, verbose_name="count"
    )

    def get_cost(self):
        return self.price * self.count


class Payment(models.Model):
    number = models.DecimalField(default=0, max_digits=16, decimal_places=0)
    name = models.CharField(max_length=100, default="card")
    month = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    year = models.DecimalField(default=0, max_digits=4, decimal_places=0)
    code = models.DecimalField(default=0, max_digits=3, decimal_places=0)
