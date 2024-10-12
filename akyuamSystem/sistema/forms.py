from django import forms
from .models import Participante

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'apellido', 'no_expediente']  # Asegúrate de incluir todos los campos necesarios

