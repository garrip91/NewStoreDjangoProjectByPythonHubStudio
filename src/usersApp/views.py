from django.shortcuts import render


def login(request):
    
    context = {
        "title": "Home - Авторизация",
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
