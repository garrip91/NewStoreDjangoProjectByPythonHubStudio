from django.shortcuts import render
from django.http import HttpResponse

from goodsApp.models import Categories


def index(request):
    
    categories = Categories.objects.all()
    
    context: dict = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    
    return render(request, "mainApp/index.html", context=context)


def about(request):
    
    context: dict = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар.",
    }
    
    return render(request, "mainApp/about.html", context=context)
