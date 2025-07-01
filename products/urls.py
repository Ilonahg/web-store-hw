from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),  # 👈 Список продуктов
    path('create/', views.create_product, name='create'),  # ✅ Добавлено!
    path('<int:pk>/', views.product_detail, name='detail'),
    path('<int:pk>/edit/', views.edit_product, name='edit'),
    path('<int:pk>/delete/', views.delete_product, name='delete'),
    path('<int:pk>/unpublish/', views.unpublish_product, name='unpublish'),
]
