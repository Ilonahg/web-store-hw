from .views import product_list, product_detail

from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]
