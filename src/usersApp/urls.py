from django.urls import path
from .views import UserLoginView, registration, profile, users_cart, logout


app_name = "usersApp"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", registration, name="registration"),
    path("profile/", profile, name="profile"),
    path("users-cart/", users_cart, name="users_cart"),
    path("logout/", logout, name="logout"),
]
