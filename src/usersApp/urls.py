from django.urls import path
from .views import login, registration, profile, users_cart, logout


app_name = "usersApp"

urlpatterns = [
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("users-cart/", users_cart, name="users_cart"),
    path("logout/", logout, name="logout"),
]
