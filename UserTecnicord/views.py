from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from UserTecnicord.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get ('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'Inicio de sesion satisfactorio!')


            else:
                messages.info(request, 'Por favor verifique los datos ingresados')
        else:

            messages.info(request, 'Inicio de sesion fallido!')

        return redirect('TecnicordInicio')

    contexto = {
        'form': AuthenticationForm(),
        'nombre_form': 'Login'
    }

    return render(request, "UserTecnicord/login.html", contexto)

def register(request):
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.info(request, 'Tu usuario fue registrado correctamente!')
        else:
            messages.info(request, 'Tu usuario no pudo ser registrado!')
        return redirect('TecnicordInicio')

    contexto = {
        # 'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
    }

    return render(request, 'UserTecnicord/login.html', contexto)