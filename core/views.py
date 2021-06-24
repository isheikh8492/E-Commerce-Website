from django.http import request
from django.shortcuts import render
from .models import Item

# Create your views here.


# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home-page.html", context)


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)


def checkout(request):
    return render(request, "checkout.html")


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)
