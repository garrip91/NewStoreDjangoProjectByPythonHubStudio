from django.urls import path
from .views import UserLoginView, UserRegistrationView, UserProfileView, UserCartView, logout


app_name = "usersApp"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", UserRegistrationView.as_view(), name="registration"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("users-cart/", UserCartView.as_view(), name="users_cart"),
    path("logout/", logout, name="logout"),
]
