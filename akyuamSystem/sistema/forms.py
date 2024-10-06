from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Municipio, Departamento

class MunicipioForm(forms.ModelForm):
    class Meta:
        model = Municipio
        fields = ['nombre', 'departamento']

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
