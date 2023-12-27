from django import forms
from .models import usuario,resultados


class RegistroForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['name']

class RegistroPuntaje(forms.ModelForm):
    class Meta:
        model = resultados
        fields = ['puntaje']