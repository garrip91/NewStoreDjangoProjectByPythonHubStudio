from django.shortcuts import render


def create_order(request):
    
    return render(request, "ordersApp/create_order.html")
