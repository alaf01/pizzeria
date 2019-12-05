from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredient, Dough_flour, Dough_size, Dough_thickness, Sauce, Pizza_compose, Pizza_menu

def index(request):
    return render(request, "add_items/index.html")

def compose(request):
    context = {
        "dough": Dough_flour.objects.all(),
        "size": Dough_size.objects.all(),
        "thickness": Dough_thickness.objects.all(),
        "sauce": Sauce.objects.all(),
        "ingredient": Ingredient.objects.all()
              }
    return render(request, "add_items/compose.html", context)

def menu(request):
    context = {
    "pizza": Pizza_menu.objects.all()
    }
    return render(request, "add_items/menu.html", context)

def myorder(request):
    context={

    }
    return render(request, "add_items/myorder.html", context)

def price(request):
    context={
    "sizes": Dough_size.objects.all(),
    }
    return render(request, "add_items/price.html", context)
