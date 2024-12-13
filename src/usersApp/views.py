from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from cartsApp.models import Cart
from ordersApp.models import Order, OrderItem


# def login(request):
    
    # if request.method == "POST":
        # form = UserLoginForm(data=request.POST)
        # if form.is_valid():
            # username = request.POST["username"]
            # password = request.POST["password"]
            # user = auth.authenticate(username=username, password=password)
            
            # session_key = request.session.session_key
            
            # if user:
                # auth.login(request, user)
                # messages.success(request, f"{username}, Вы вошли в свой аккаунт!")
                
                # if session_key:
                    # Cart.objects.filter(session_key=session_key).update(user=user)
                
                # redirect_page = request.POST.get("next", None)
                # if redirect_page and redirect_page != reverse("usersApp:logout"):
                    # return HttpResponseRedirect(request.POST.get("next"))
                
                # return HttpResponseRedirect(reverse("mainApp:index"))
    # else:
        # form = UserLoginForm()
    
    # context = {
        # "title": "Home - Авторизация",
        # "form": form,
    # }
    
    # return render(request, "usersApp/login.html", context=context)


class UserLoginView(LoginView):
    
    template_name = "usersApp/login.html"
    form_class = UserLoginForm
    # success_url = reverse_lazy("mainApp:index")
    
    def get_success_url(self):
        redirect_page = self.request.POST.get("next", None)
        if redirect_page and redirect_page != reverse("user:logout"):
            return redirect_page
        return reverse_lazy("mainApp:index")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Авторизация"
        return context


def registration(request):
    
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            session_key = request.session.session_key
            
            user = form.instance
            auth.login(request, user)
            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            
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
    
    orders = (
        Order.objects.filter(user=request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        )
        .order_by("-id")
    )
    
    context = {
        "title": "Home - Кабинет",
        "form": form,
        "orders": orders
    }
    
    return render(request, "usersApp/profile.html", context=context)


def users_cart(request):
    
    return render(request, "usersApp/users_cart.html")


@login_required
def logout(request):
    
    messages.success(request, f"{request.user.username}, Вы вышли из своего аккаунта!")
    auth.logout(request)
    
    return redirect(reverse("mainApp:index"))
