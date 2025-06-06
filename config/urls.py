from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # маршруты из приложения users
    path('', TemplateView.as_view(template_name='menu.html'), name='home'),  # главная страница
]
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', TemplateView.as_view(template_name='menu.html'), name='home'),
    path('contacts/', TemplateView.as_view(template_name='contacts.html'), name='contacts'),  # ← вот это
]
