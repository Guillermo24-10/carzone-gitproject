from django.shortcuts import render
from .models import Equipo
from carros.models import Carro
# Create your views here.

def home(request):
    equipo = Equipo.objects.all()
    carro = Carro.objects.order_by('-fec_creacion').filter(destacado=True)
    allcarros = Carro.objects.order_by('-fec_creacion')    
    modelo_search = Carro.objects.values_list('modelo',flat=True).distinct()## DATOS UNICOS PARA Q NO SE REPITAN
    ciudad_search = Carro.objects.values_list('ciudad',flat=True).distinct()
    year_search = Carro.objects.values_list('year',flat=True).distinct()
    cuerpo_search = Carro.objects.values_list('estilo_cuerpo',flat=True).distinct()
    data = {
        'equipo':equipo,  ## tiene que ser igual el nombre
        'carro':carro,  ## tiene que ser igual el nombre
        'allcarros':allcarros,
        'modelo_search':modelo_search,
        'ciudad_search':ciudad_search,
        'year_search':year_search,
        'cuerpo_search':cuerpo_search,
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
