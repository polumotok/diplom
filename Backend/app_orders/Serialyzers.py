from rest_framework import serializers
from app_orders.models import Orders, Order_product, Payment


class OrderProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="product.id")
    category = serializers.CharField(source="product.category")
    price = serializers.IntegerField(source="product.price")
    title = serializers.CharField(source="product.title")
    href = serializers.CharField(source="product.href")
    count = serializers.IntegerField()
    images = serializers.StringRelatedField(many=True, source="product.images")

    class Meta:
        model = Order_product
        fields = ["id", "category", "price", "title", "href", "count", "images"]


class OrderingGetSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source="profile.fullName")
    email = serializers.CharField(source="profile.email")
    phone = serializers.CharField(source="profile.phone")
    products = OrderProductSerializer(many=True)

    class Meta:
        model = Orders
        fields = [
            "orderId",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        ]


class OrderingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_product
        fields = ["count"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
