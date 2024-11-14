from django.shortcuts import render

from .models import Products


def catalog(request):
    
    goods = Products.objects.all()
    
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    
    return render(request, "goodsApp/catalog.html", context=context)


def product(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    
    return render(request, "goodsApp/product.html", context=context)
