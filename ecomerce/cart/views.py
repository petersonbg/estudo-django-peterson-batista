from django.shortcuts import render

def cart_datails(request):
    return render(request, 'cart/cart_detail.html')
