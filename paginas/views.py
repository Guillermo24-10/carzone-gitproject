from django.shortcuts import render
from .models import Equipo
# Create your views here.

def home(request):
    equipo = Equipo.objects.all()
    data = {
        'equipo':equipo,
    }
    return render(request, 'paginas/home.html', data)

def about(request):
    equipo = Equipo.objects.all()
    data = {
        'equipo':equipo,
    }
    return render(request, 'paginas/about.html', data)

def servicios(request):
    return render(request, 'paginas/servicios.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')
