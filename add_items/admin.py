from django.contrib import admin
from . models import Ingredient, Dough_flour, Dough_size, Dough_thickness, Sauce, Pizza_menu
# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Dough_flour)
admin.site.register(Dough_size)
admin.site.register(Dough_thickness)
admin.site.register(Sauce)
admin.site.register(Pizza_menu)
