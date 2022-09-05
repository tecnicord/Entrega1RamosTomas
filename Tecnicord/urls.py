from django.urls import path
from Tecnicord.views import tractores, inicio, camiones, pulverizadoras

urlpatterns = [
        path('tractores/', tractores, name='TecnicordTractores'),
        path('camiones/', camiones, name='TecnicordCamiones'),
        path('pulverizadoras/', pulverizadoras, name='TecnicordPulverizadoras'),
        path ('', inicio, name='TecnicordInicio'),
]
