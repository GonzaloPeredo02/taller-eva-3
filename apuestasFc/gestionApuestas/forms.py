
from django import forms
from .models import Juego, Equipo

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['equipo1', 'equipo2']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais']
