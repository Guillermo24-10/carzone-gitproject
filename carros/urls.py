from django.urls import path
from . import views

urlpatterns = [
    path('', views.carros, name='carros'),
    path('<int:id>', views.car_detalle, name='car_detalle'),
    path('search', views.search, name='search'),
]
