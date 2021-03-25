from django.shortcuts import render

# Create your views here.

def carros(request):
    return render(request, 'carros/carros.html')
