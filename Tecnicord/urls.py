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
        path('busqueda_potencia_post/', busqueda_potencia_post, name= 'TecnicordBusquedaPotenciaPost'),
        path('busqueda_carga/', busqueda_carga, name='TecnicordBusquedaCarga'),
        path('busqueda_carga_post/', busqueda_carga_post, name='TecnicordBusquedaCargaPost'),
        path('busqueda_litros/', busqueda_litros, name='TecnicordBusquedaLitros'),
        path('busqueda_litros_post/', busqueda_litros_post, name='TecnicordBusquedaLitrosPost'),
        path('eliminar_tractor/<int:potencia>', eliminar_tractores, name='TecnicordEliminarTractor'),
        path('eliminar_camion/<int:carga>', eliminar_camiones, name='TecnicordEliminarCamion'),
        path('eliminar_pulverizadora/<int:litros>', eliminar_pulverizadoras, name='TecnicordEliminarPulverizadora'),
]
