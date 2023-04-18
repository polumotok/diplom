from rest_framework import serializers

from app_products.models import Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    href = serializers.SerializerMethodField()
    class Meta:
        model = Subcategory
        fields = ["id", "title", "image", "href"]

    def get_href(self, obj):
        return (f'/catalog/{obj.id}')
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    href = serializers.SerializerMethodField()
    subcategories = SubcategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ["id", "title", "image", "href", 'subcategories']

    def get_href(self, obj):
        return (f'/catalog/{obj.id}')



