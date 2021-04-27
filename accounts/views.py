from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacto.models import Contacto


# Create your views here.

def login(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=usuario, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'se conectó con éxito')
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales de acceso invalidos')
            return redirect('login')

    return render(request,'accounts/login.html')

def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['firstname']
        apellido = request.POST['lastname']
        usuario = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'Username ya existe')
                return redirect('registrar')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email ya existe')
                    return redirect('registrar')
                else:
                    user = User.objects.create_user(first_name=nombre, last_name=apellido,email=email, username=usuario, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Logueado con éxito')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Estás registrado con éxito.')
                    return redirect('login')
        else:
            messages.error(request, 'la contraseña no coincide')
            return redirect('registrar')
    else:
        return render(request,'accounts/registrar.html')



def cerrar_sesion(request):
    if request.method == 'POST':
        auth.logout(request)
        #messages.success(request, 'se desconectó con éxito')
        return redirect('home')
    return render(request,'accounts/login.html')

def dashboard(request):
    user_consulta = Contacto.objects.order_by('-fecha_creacion').filter(user_id=request.user.id)
    data = {
            'consultas' : user_consulta,
    }
    return render(request,'accounts/dashboard.html', data)
