from django.urls import path
from Tecnicord.views import tractores, inicio, camiones, pulverizadoras, tractores_formulario, camiones_formulario, pulverizadoras_formulario

urlpatterns = [
        path('tractores/', tractores, name='TecnicordTractores'),
        path('camiones/', camiones, name='TecnicordCamiones'),
        path('pulverizadoras/', pulverizadoras, name='TecnicordPulverizadoras'),
        path ('', inicio, name='TecnicordInicio'),
        path('tractores_formulario/', tractores_formulario, name= 'TecnicordTractoresFormulario'),
        path('camiones_formulario/', camiones_formulario, name= 'TecnicordCamionesFormulario'),
        path('pulverizadoras_formulario/', pulverizadoras_formulario, name= 'TecnicordPulverizadorasFormulario'),]
