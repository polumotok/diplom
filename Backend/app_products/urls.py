from django.urls import path

from django.views.generic import TemplateView

from app_products.views import CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='test'),
    ]
