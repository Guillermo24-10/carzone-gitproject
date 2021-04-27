from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('paginas.urls')),
    path('carros/', include('carros.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccount/', include('allauth.urls')),
    path('contacto/', include('contacto.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
