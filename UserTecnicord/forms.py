from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Apellido = forms.CharField()
    Nombre = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'Apellido', 'Nombre')