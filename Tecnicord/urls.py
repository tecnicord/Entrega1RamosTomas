from django.urls import path
from Tecnicord.views import tractores, inicio

urlpatterns = [
        path('tractores/', tractores),
        path ('', inicio),
]
