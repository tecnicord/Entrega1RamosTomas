from django.shortcuts import render, redirect
from Tecnicord.forms import TractoresFormulario, CamionesFormulario, PulverizadorasFormulario, BusquedaPotenciaFormulario
from Tecnicord.models import Tractores, Camiones, Pulverizadoras


def busqueda_potencia_post(request):
    potencia = request.GET.get('potencia')

    tractores = Tractores.objects.filter(potencia__icontains=potencia)
    contexto =  {
        'tractores': tractores
    }

    return render (request, 'Tecnicord/potencia_filtrado.html', contexto)
def busqueda_potencia(request):

    contexto = {
        'form': BusquedaPotenciaFormulario(),
    }

    return render (request, 'Tecnicord/busqueda_potencia.html', contexto)




def tractores(request):
    tractores1 = Tractores(nombre="6180", potencia=180)
    tractores1.save()
    contexto = {
        'tractores': tractores1
    }
    return render(request, 'Tecnicord/tractores.html', contexto)

def camiones(request):
    camiones1 = Camiones(nombre="8700", carga=7000)
    camiones1.save()
    contexto = {
        'camiones': camiones1
    }
    return render(request, 'Tecnicord/camiones.html', contexto)

def pulverizadoras(request):
    pulverizadoras1 = Pulverizadoras(nombre="Stronger", litros=3000)
    pulverizadoras1.save()
    contexto = {
        'pulverizadoras': pulverizadoras1
    }
    return render(request, 'Tecnicord/pulverizadoras.html', contexto)

def inicio(request):

    return render (request, 'index.html')

def tractores_formulario(request):

    if request.method == 'POST':
        mi_formulario = TractoresFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            tractores1 = Tractores(nombre=data.get('nombre'), potencia=data.get('potencia'))
            tractores1.save()

            return redirect('TecnicordTractoresFormulario')

    tractores = Tractores.objects.all()


    contexto = {
        'form': TractoresFormulario(),
        'tractores': tractores
    }
    return render(request, 'Tecnicord/tractores_formulario.html', contexto)

def camiones_formulario(request):

    if request.method == 'POST':
        mi_formulario = CamionesFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            camiones1 = Camiones(nombre=data.get('nombre'), carga=data.get('carga'))
            camiones1.save()

            return redirect('TecnicordInicio')
    contexto = {
        'form': CamionesFormulario()
    }
    return render(request, 'Tecnicord/camiones_formulario.html', contexto)

def pulverizadoras_formulario(request):
    if request.method == 'POST':
        mi_formulario = PulverizadorasFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            pulverizadoras1 = Pulverizadoras(nombre=data.get('nombre'), litros=data.get('litros'))
            pulverizadoras1.save()

            return redirect('TecnicordInicio')
    contexto = {
        'form': PulverizadorasFormulario()
    }
    return render(request, 'Tecnicord/pulverizadoras_formulario.html', contexto)