from django.shortcuts import render
from Tecnicord.models import Tractores, Camiones, Pulverizadoras

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
