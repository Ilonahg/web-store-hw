from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include  # ← Этого не хватает!

urlpatterns = [
    path('', include('catalog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
