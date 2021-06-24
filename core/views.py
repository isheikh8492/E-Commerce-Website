from typing import List
from django.http import request
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Item
from django.views.generic import ListView

# Create your views here.


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)
