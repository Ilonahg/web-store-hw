from .views import product_list, product_detail

from django.urls import path
from .views import product_detail, product_list
from django.shortcuts import render

urlpatterns = [
    path("", product_list, name="product_list"),
    path("products/<int:pk>/", product_detail, name="product_detail"),
]

from .views import product_detail  # убери product_list, если не нужен

from .views import product_list, product_detail

urlpatterns = [
    path("", product_list, name="index"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]


def contacts(request):
    return render(request, "contacts.html")
