# products/urls.py

from django.urls import path
from .views import products_by_category_view

urlpatterns = [
    path('category/<int:category_id>/', products_by_category_view, name='products_by_category'),
]
