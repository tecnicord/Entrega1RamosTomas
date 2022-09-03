from django.shortcuts import render
from Tecnicord.models import Tractores

def tractores(request):
    tractores1 = Tractores(nombre="6180", potencia=180)
    tractores1.save()
    contexto = {
        'tractores': tractores1
    }
    return render(request, 'tractores.html', contexto)
