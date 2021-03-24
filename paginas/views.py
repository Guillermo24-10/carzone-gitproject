from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'paginas/home.html')

def about(request):
    return render(request, 'paginas/about.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')
