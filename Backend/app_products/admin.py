from django.contrib import admin

from app_products.models import Category, Subcategory, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')





admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)


