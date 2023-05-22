from django.contrib import admin

from app_products.models import (
    Category,
    Subcategory,
    Product,
    ProductImage,
    tags,
    specifications,
)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"href": ("title",)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    prepopulated_fields = {"href": ("title",)}


class ProductInLine(admin.StackedInline):
    model = ProductImage


class TagsInLine(admin.StackedInline):
    model = tags


class SpecificationInLine(admin.StackedInline):
    model = specifications


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
        TagsInLine,
        SpecificationInLine,
    ]
    list_display = ("id", "title")
    # prepopulated_fields = {"href": ("title",)}
    fieldsets = [
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "fullDescription",
                    "price",
                    "count",
                    "href",
                    "category",
                ),
            },
        ),
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
