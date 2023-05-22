from django.urls import path


from app_products.views import (
    CategoryView,
    ProductPopularView,
    CatalogView,
    ProductLimitedView,
    ProductSalesView,
    ProductBannersView,
    ProductDetailView,
    basket,
    ReviewView,
)

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="category"),
    path("banners/", ProductBannersView.as_view(), name="banners"),
    path("products/popular/", ProductPopularView.as_view(), name="popular"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="Detail_view"),
    path("products/limited/", ProductLimitedView.as_view(), name="limited"),
    path("sales/", ProductSalesView.as_view(), name="sales"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("basket/", basket.as_view(), name="backet"),
    path("product/<int:pk>/review", ReviewView.as_view(), name="review"),
]
