from django.urls import path
from mainApp.views import index, about


app_name = "mainApp"

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
]
