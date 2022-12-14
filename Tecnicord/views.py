from django.shortcuts import render, redirect
from Tecnicord.forms import TractoresFormulario, CamionesFormulario, PulverizadorasFormulario, BusquedaPotenciaFormulario, BusquedaCargaFormulario, BusquedaLitrosFormulario
from Tecnicord.models import Tractores, Camiones, Pulverizadoras
from django.contrib import messages
import django
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def editar_tractores(request, potencia):
    tractores_editar = Tractores.objects.get(potencia=potencia)

    if request.method == 'POST':
        mi_formulario = TractoresFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            tractores_editar.nombre = data.get('nombre')
            tractores_editar.potencia = data.get('potencia')
            try:
                tractores_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion falló, por repetido")



            return redirect('TecnicordTractores')

    contexto = {
        'form': TractoresFormulario(
            initial={
                "nombre": tractores_editar.nombre,
                "potencia": tractores_editar.potencia
            }
        )
    }
    return render(request, 'Tecnicord/tractores_formulario.html', contexto)

def editar_camiones(request, carga):
    camiones_editar = Camiones.objects.get(carga=carga)

    if request.method == 'POST':
        mi_formulario = CamionesFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            camiones_editar.nombre = data.get('nombre')
            camiones_editar.carga = data.get('carga')
            try:
                camiones_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion falló, por repetido")


            return redirect('TecnicordCamiones')

    contexto = {
        'form': CamionesFormulario(
            initial={
                "nombre": camiones_editar.nombre,
                "carga": camiones_editar.carga
            }
        )
    }

    return render(request, 'Tecnicord/camiones_formulario.html', contexto)
def editar_pulverizadoras(request, litros):
    pulverizadoras_editar = Pulverizadoras.objects.get(litros=litros)

    if request.method == 'POST':
        mi_formulario = PulverizadorasFormulario(request.POST)

        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data

            pulverizadoras_editar.nombre = data.get('nombre')
            pulverizadoras_editar.litros = data.get('litros')
            try:
                pulverizadoras_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "La modificacion falló, por repetido")

            return redirect('TecnicordPulverizadoras')

    contexto = {
        'form': PulverizadorasFormulario(
            initial={
                "nombre": pulverizadoras_editar.nombre,
                "litros": pulverizadoras_editar.litros
            }
        )
    }
    return render(request, 'Tecnicord/pulverizadoras_formulario.html', contexto)


def eliminar_tractores(request, potencia):
    tractor_eliminar = Tractores.objects.get(potencia=potencia)
    tractor_eliminar.delete()
    messages.info(request, f"El Tractor {tractor_eliminar} fue eliminado")

    return redirect ("TecnicordTractores")

def eliminar_camiones(request, carga):
    camion_eliminar = Camiones.objects.get(carga=carga)
    camion_eliminar.delete()
    messages.info(request, f"El Camion {camion_eliminar} fue eliminado")
    return redirect ("TecnicordCamiones")

def eliminar_pulverizadoras(request, litros):
    pulverizadora_eliminar = Pulverizadoras.objects.get(litros=litros)
    pulverizadora_eliminar.delete()
    messages.info(request, f"La Pulverizadora {pulverizadora_eliminar} fue eliminada")

    return redirect ("TecnicordPulverizadoras")

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

def busqueda_carga_post(request):
    carga = request.GET.get('carga')

    camiones = Camiones.objects.filter(carga__icontains=carga)
    contexto =  {
        'camiones': camiones
    }

    return render (request, 'Tecnicord/carga_filtrado.html', contexto)
def busqueda_carga(request):

    contexto = {
        'form': BusquedaCargaFormulario(),
    }

    return render (request, 'Tecnicord/busqueda_carga.html', contexto)


def busqueda_litros_post(request):
    litros = request.GET.get('litros')

    pulverizadoras = Pulverizadoras.objects.filter(litros__icontains=litros)
    contexto =  {
        'pulverizadoras': pulverizadoras
    }

    return render (request, 'Tecnicord/litros_filtrado.html', contexto)
def busqueda_litros(request):

    contexto = {
        'form': BusquedaLitrosFormulario(),
    }

    return render (request, 'Tecnicord/busqueda_litros.html', contexto)


class TractoresList(LoginRequiredMixin,ListView):
    model = Tractores
    template_name = 'Tecnicord/tractores.html'

#def tractores(request):
 #   tractores = Tractores.objects.all()
  #  contexto =  {
   #     'tractores' : tractores
    #}
    #return render(request, 'Tecnicord/tractores.html', contexto)

class CamionesList(LoginRequiredMixin,ListView):
    model = Camiones
    template_name = 'Tecnicord/camiones.html'

#def camiones(request):
 #   camiones = Camiones.objects.all()
  #  contexto =  {
   #     'camiones' : camiones
    #}
    #return render(request, 'Tecnicord/camiones.html', contexto)

class PulverizadorasList(LoginRequiredMixin,ListView):
    model = Pulverizadoras
    template_name = 'Tecnicord/pulverizadoras.html'

#def pulverizadoras(request):
 #   pulverizadoras = Pulverizadoras.objects.all()
  #  contexto =  {
   #     'pulverizadoras' : pulverizadoras
    #}
    #return render(request, 'Tecnicord/pulverizadoras.html', contexto)

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




    contexto = {
        'form': TractoresFormulario()
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