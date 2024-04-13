from django import forms
from .models import Usuario

class Registro_form(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput())
    id_tipo_usuario = 2

    class Meta:
        model = Usuario
        fields = ['username', 'useremail', 'password', 'id_tipo_usuario']
