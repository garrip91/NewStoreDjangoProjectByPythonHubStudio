from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в свой аккаунт!")
                
                if request.POST.get("next", None):
                    return HttpResponseRedirect(request.POST.get("next"))
                
                return HttpResponseRedirect(reverse("mainApp:index"))
    else:
        form = UserLoginForm()
    
    context = {
        "title": "Home - Авторизация",
        "form": form,
    }
    
    return render(request, "usersApp/login.html", context=context)


def registration(request):
    
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы зарегистрированы и вошли в свой аккаунт!")
            return HttpResponseRedirect(reverse("mainApp:index"))
    else:
        form = UserRegistrationForm()
    
    context = {
        "title": "Home - Регистрация",
        "form": form,
    }
    
    return render(request, "usersApp/registration.html", context=context)


@login_required
def profile(request):
    
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{username}, Профиль Вашего аккаунта успешно обновлён!")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        "title": "Home - Кабинет",
        "form": form,
    }
    
    return render(request, "usersApp/profile.html", context=context)


def users_cart(request):
    
    return render(request, "usersApp/users_cart.html")


@login_required
def logout(request):
    
    messages.success(request, f"{request.user.username}, Вы вышли из своего аккаунта!")
    auth.logout(request)
    
    return redirect(reverse("mainApp:index"))
