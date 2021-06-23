from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, View

# Create your views here.


# def item_list(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home-page.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home.html"


class CheckoutView(View):
    def get(self, *args, **kwargs):
        context = {}
        return render(self.request, "checkout-page.html", context)
