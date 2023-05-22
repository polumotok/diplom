from rest_framework import serializers
from app_products.models import (
    Category,
    Subcategory,
    Product,
    Cart,
    specifications,
    tags,
    Review,
)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class SubcategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    href = serializers.SerializerMethodField()

    class Meta:
        model = Subcategory
        fields = ["id", "title", "image", "href"]

    def get_href(self, obj):
        return f"/catalog/{obj.id}"


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    href = serializers.SerializerMethodField()
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "title", "image", "href", "subcategories"]

    def get_href(self, obj):
        return f"/catalog/{obj.id}"


class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = specifications
        fields = ["name", "value"]


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tags
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    category = serializers.SerializerMethodField()
    href = serializers.SerializerMethodField()
    images = serializers.StringRelatedField(many=True)
    count = serializers.IntegerField()
    price = serializers.IntegerField()
    tags = serializers.StringRelatedField(many=True)
    specifications = SpecificationsSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "title",
            "description",
            "fullDescription",
            "href",
            "images",
            "tags",
            "specifications",
            "reviews",
        ]

    def get_category(self, obj):
        return f"/catalog/{obj.category}"

    def get_href(self, obj):
        return f"/product/{obj.id}"


class CartSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="product.id")
    category = serializers.CharField(source="product.category")
    price = serializers.IntegerField(source="product.price")
    title = serializers.CharField(source="product.title")
    href = serializers.CharField(source="product.href")
    count = serializers.IntegerField()
    images = serializers.StringRelatedField(many=True, source="product.images")

    class Meta:
        model = Cart
        fields = ["id", "category", "price", "count", "title", "href", "images"]
