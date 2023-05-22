from django.urls import path

from app_orders.views import OrdersView, OrderActiveView, OrderRegisterView, PaymentView

urlpatterns = [
    path("orders", OrdersView.as_view(), name="category"),
    path("orders/<int:pk>/", OrderRegisterView.as_view(), name="OrderRegisterView"),
    path("orders/active", OrderActiveView.as_view(), name="category"),
    path("payment/", PaymentView.as_view(), name="category"),
]
