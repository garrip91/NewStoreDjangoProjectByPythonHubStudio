from django.urls import path
from .views import catalog, product


app_name = "goodsApp"

urlpatterns = [
    path("search/", catalog, name="search"),
    path("<slug:category_slug>/", catalog, name="index"),
    path("product/<slug:product_slug>/", product, name="product"),
]
