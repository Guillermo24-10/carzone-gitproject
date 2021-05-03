from django.shortcuts import render,redirect
from .models import Equipo
from carros.models import Carro
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
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
    if request.method == 'POST':
        nombre = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        telefono = request.POST['phone']
        mensaje = request.POST['message']

        email_subject = 'Tiene un nuevo mensaje del sitio web de carzone sobre: '+ subject
        mensaje_body = 'Nombre: '+ nombre + '. Email: '+ email + '. Telefono: '+ telefono + '. mensaje: '+ mensaje

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                mensaje_body,
                'pgaugusto24@gmail.com',
                [admin_email],
                fail_silently=False,
                )
        messages.success(request, 'Gracias por contactarnos. Nos pondremos en contacto con usted en breve')
        return redirect('contacto')

    return render(request, 'paginas/contacto.html')
