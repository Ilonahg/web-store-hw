from django.contrib import admin
from .models import Product  # или твоя модель, если имя другое

admin.site.register(Product)
