from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm


def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("mainApp:index"))
    else:
        form = UserLoginForm()
    
    context = {
        "title": "Home - Авторизация",
        "form": form,
    }
    
    return render(request, "usersApp/login.html", context=context)


def registration(request):
    
    context = {
        "title": "Home - Регистрация",
    }
    
    return render(request, "usersApp/registration.html", context=context)


def profile(request):
    
    context = {
        "title": "Home - Кабинет",
    }
    
    return render(request, "usersApp/profile.html", context=context)


def logout(request):
    
    context = {
        "title": "Home - Авторизация",
    }
    
    return render(request, "", context=context)
