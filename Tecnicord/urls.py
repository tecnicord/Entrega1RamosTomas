from django.urls import path
from Tecnicord.views import *
urlpatterns = [
        path('tractores/', tractores, name='TecnicordTractores'),
        path('camiones/', camiones, name='TecnicordCamiones'),
        path('pulverizadoras/', pulverizadoras, name='TecnicordPulverizadoras'),
        path ('', inicio, name='TecnicordInicio'),
        path('tractores_formulario/', tractores_formulario, name= 'TecnicordTractoresFormulario'),
        path('camiones_formulario/', camiones_formulario, name= 'TecnicordCamionesFormulario'),
        path('pulverizadoras_formulario/', pulverizadoras_formulario, name= 'TecnicordPulverizadorasFormulario'),
        path('busqueda_potencia/', busqueda_potencia, name= 'TecnicordBusquedaPotencia'),
        path('busqueda_potencia_post/', busqueda_potencia_post, name= 'TecnicordBusquedaPotenciaPost'),]
