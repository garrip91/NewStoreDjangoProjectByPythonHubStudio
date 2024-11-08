from django.urls import path
from .views import catalog, product


app_name = "goodsApp"

urlpatterns = [
    path("", catalog, name="index"),
    path("product/", product, name="product"),
]
