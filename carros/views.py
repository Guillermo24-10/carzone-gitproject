from django.shortcuts import render, get_object_or_404
from .models import Carro
from django.core.paginator import  EmptyPage, PageNotAnInteger, Paginator ## IMPORTS PARA PAGINACION


# Create your views here.
# =========================CARROS====================================
def carros(request):
    carros = Carro.objects.order_by('-fec_creacion')
    paginator = Paginator(carros, 4) ## 4 CARROS POR PAGINA
    page = request.GET.get('page')
    page_carro = paginator.get_page(page)

    modelo_search = Carro.objects.values_list('modelo',flat=True).distinct()## DATOS UNICOS PARA Q NO SE REPITAN
    ciudad_search = Carro.objects.values_list('ciudad',flat=True).distinct()
    year_search = Carro.objects.values_list('year',flat=True).distinct()
    cuerpo_search = Carro.objects.values_list('estilo_cuerpo',flat=True).distinct()

    data = {
        'carros': page_carro,
        'modelo_search': modelo_search,
        'ciudad_search': ciudad_search,
        'year_search': year_search,
        'cuerpo_search': cuerpo_search,
    }
    return render(request, 'carros/carros.html',data)
# =========================CARROS====================================

# =========================DETALLE_CARRO====================================
def car_detalle(request, id):
    single_car = get_object_or_404(Carro, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'carros/car_detalle.html', data)

# =========================BUSCAR_CARRO====================================

def search(request):
    carro = Carro.objects.order_by('-fec_creacion')

    modelo_search = Carro.objects.values_list('modelo',flat=True).distinct()## DATOS UNICOS PARA Q NO SE REPITAN
    ciudad_search = Carro.objects.values_list('ciudad',flat=True).distinct()
    year_search = Carro.objects.values_list('year',flat=True).distinct()
    cuerpo_search = Carro.objects.values_list('estilo_cuerpo',flat=True).distinct()
    transmission_search = Carro.objects.values_list('transmission',flat=True).distinct()

    if 'modelo' in request.GET:
        modelo = request.GET['modelo']
        if modelo:
            carro = carro.filter(modelo__iexact=modelo)

    if 'ciudad' in request.GET:
        ciudad = request.GET['ciudad']
        if ciudad:
            carro = carro.filter(ciudad__iexact=ciudad)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            carro = carro.filter(year__iexact=year)

    if 'estilo_cuerpo' in request.GET:
        estilo_cuerpo = request.GET['estilo_cuerpo']
        if estilo_cuerpo:
            carro = carro.filter(estilo_cuerpo__iexact=estilo_cuerpo)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            carro = carro.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            carro = carro.filter(precio__gte=min_price, precio__lte=max_price)

    data = {
        'carro':carro,
        'modelo_search': modelo_search,
        'ciudad_search': ciudad_search,
        'year_search': year_search,
        'cuerpo_search': cuerpo_search,
        'transmission_search': transmission_search,
    }
    return render(request, 'carros/search.html', data)

# =========================CARROS====================================
