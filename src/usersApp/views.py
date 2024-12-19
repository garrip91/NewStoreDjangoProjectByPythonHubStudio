from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

from .forms import UserLoginForm, UserRegistrationForm, ProfileForm
from cartsApp.models import Cart
from ordersApp.models import Order, OrderItem
from common.mixins import CacheMixin


class UserLoginView(LoginView):
    
    template_name = "usersApp/login.html"
    form_class = UserLoginForm
    # success_url = reverse_lazy("mainApp:index")
    
    def get_success_url(self):
        redirect_page = self.request.POST.get("next", None)
        if redirect_page and redirect_page != reverse("user:logout"):
            return redirect_page
        return reverse_lazy("mainApp:index")
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        
        user = form.get_user()
        
        if user:
            auth.login(self.request, user)
            if session_key:
                # delete old authorized user carts:
                forgot_carts = Cart.objects.filter(user=user)
                if forgot_carts.exists():
                    forgot_carts.delete()
                # add new authorized user carts from anonimous session:
                Cart.objects.filter(session_key=session_key).update(user=user)
                
                messages.success(self.request, f"{user.username}, Вы вошли в аккаунт!")
        
                return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Авторизация"
        return context


class UserRegistrationView(CreateView):
    template_name = "usersApp/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("usersApp:profile")
    
    def form_valid(self, form):
        session_key = self.request.session.session_key
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user)
            
        if session_key:
            Cart.objects.filter(session_key=session_key).update(user=user)
            
        messages.success(self.request, f"{user.username}, Вы успешно зарегистрированы и вошли в свой аккаунт!")
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Регистрация"
        return context


class UserProfileView(LoginRequiredMixin, CacheMixin, UpdateView):
    template_name = "usersApp/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("usersApp:profile")
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Ваш профиль успешно обновлён!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Прозошла ошибка!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Кабинет"
        
        
        orders = Order.objects.filter(user=self.request.user).prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        ).order_by("-id")
        
            
        context["orders"] = self.set_get_cache(orders, f"user_{self.request.user.id}_orders", 60 * 2)
        return context


class UserCartView(TemplateView):
    template_name = "usersApp/users_cart.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Корзина"
        return context


@login_required
def logout(request):
    
    messages.success(request, f"{request.user.username}, Вы вышли из своего аккаунта!")
    auth.logout(request)
    
    return redirect(reverse("mainApp:index"))
