from django.urls import path

from .views import CreateOrderView


app_name = "ordersApp"

urlpatterns = [
    path("create-order/", CreateOrderView.as_view(), name="create_order"),
]
