from django.shortcuts import render

from .models import Products


def catalog(request):
    
    goods = Products.objects.all()
    
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    
    return render(request, "goodsApp/catalog.html", context=context)


def product(request):
    
    return render(request, "goodsApp/product.html")
