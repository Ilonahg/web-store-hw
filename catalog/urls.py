from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ContactsView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="index"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
]
