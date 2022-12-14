from django import forms

class TractoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    potencia = forms.IntegerField()

class CamionesFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    carga = forms.IntegerField()

class PulverizadorasFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    litros = forms.IntegerField()

class BusquedaPotenciaFormulario(forms.Form):
    potencia = forms.IntegerField()

class BusquedaCargaFormulario(forms.Form):
    carga = forms.IntegerField()

class BusquedaLitrosFormulario(forms.Form):
    litros = forms.IntegerField()