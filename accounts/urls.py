from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('registrar', views.registrar, name='registrar'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('dashboard', views.dashboard, name='dashboard'),
]
