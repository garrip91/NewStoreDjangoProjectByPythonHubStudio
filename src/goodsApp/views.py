from django.shortcuts import render


def catalog(request):
    
    return render(request, "goodsApp/catalog.html")


def product(request):
    
    return render(request, "goodsApp/product.html")
