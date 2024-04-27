from django import forms
from .models import Usuario
from pathlib import Path

class Registro_form(forms.ModelForm):
    id_tipo_usuario = 2

    class Meta:
        model = Usuario
        fields = ['username', 'useremail', 'password','id_tipo_usuario']
