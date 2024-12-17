from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect

def login_request(request):
    msg_login = ""
    # Verificar si el método es POST
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():  # Si el formulario es válido, autenticar al usuario
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:  # Si el usuario existe, iniciar sesión
                login(request, user)
                return redirect('inicio')  # Redirige a la página de inicio (ajusta la URL según corresponda)

            # Si la autenticación falla, mostrar un mensaje de error
            msg_login = "Usuario o contraseña incorrectos. ¿Te has equivocado?"

        else:
            # Si el formulario no es válido, mostrar un mensaje genérico
            msg_login = "Por favor, ingresa los datos correctamente."
        
    else:
        form = AuthenticationForm()

    # Enviar el formulario y el mensaje a la plantilla
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})



def register(request):
    
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"App/inicio.html")
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})