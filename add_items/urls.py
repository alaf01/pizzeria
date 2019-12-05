from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("compose/", views.compose),
    path("menu/", views.menu),
    path("price/", views.price)
]
