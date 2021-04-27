from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contacto
from django.core.mail import send_mail
from django.contrib.auth.models import User

def consulta(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_tittle = request.POST['car_tittle']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        ciudad = request.POST['ciudad']
        estado = request.POST['estado']
        email = request.POST['email']
        telefono = request.POST['telefono']
        mensaje = request.POST['mensaje']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacto.objects.all().filter(car_id=car_id,user_id=user_id)

            if has_contacted:
                messages.error(request, 'Ya ha realizado una consulta sobre este coche. Espere hasta que nos comuniquemos con usted.')
                return redirect('/carros/'+car_id)

        contacto = Contacto(car_id=car_id,car_tittle=car_tittle,user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need,
        ciudad=ciudad, estado=estado, email=email, telefono=telefono, mensaje=mensaje)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'Consulta de coche nuevo',
                'Tienes una nueva consulta para el coche. ' + car_tittle + '. Inicie sesión en su panel de administración para obtener más información',
                'pgaugusto24@gmail.com',
                [admin_email],
                fail_silently=False,
                )

        contacto.save()
        messages.success(request, 'Su solicitud ha sido enviada, nos comunicaremos con usted a la brevedad.')
        return redirect('/carros/'+car_id)
