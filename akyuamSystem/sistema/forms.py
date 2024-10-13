from django import forms
from .models import Participante
from .models import Idioma
from .models import Hijo
from .models import ReferenciaFamiliar
from .models import Hecho
from .models import Agresor
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = _("Contraseña actual")
        self.fields['new_password1'].label = _("Nueva contraseña")
        self.fields['new_password2'].label = _("Confirmar nueva contraseña")
        self.fields['new_password1'].help_text = _("Debe tener al menos 8 caracteres y no puede ser muy común.")
        self.fields['new_password2'].help_text = _("Introduce nuevamente la nueva contraseña.")

        # Aplicar clases de Bootstrap a los campos
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Correo', 'class': 'editable', 'disabled': 'disabled'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'editable', 'disabled': 'disabled'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'editable'  # Añade la clase editable
            field.widget.attrs['disabled'] = 'disabled' 

class AgresorForm(forms.ModelForm):
    class Meta:
        model = Agresor
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'dpi',
            'caracteristicas_fisicas',
            'lectura_escritura',
            'direccion',
            'actividad_laboral',
            'nombre_lugar_trabajo',
            'direccion_trabajo',
            'telefono_trabajo',
            'ingreso_mensual',
            'posee_bienes',
            'otros_bienes',
            'antecedentes_conflictividad',
            'otros_antecedentes_conflic',
            'antecedentes_enfermedad',
            'descripcion_enfermedad',
            'dependencias_adictivas',
            'otras_dependencias',
            'usa_armas',
            'descripcion_armas',
            'referencias_personales',
            'observaciones',
            'dependencia',
            'escolaridad',
            'estado_civil',
            'etnia',
            'municipio_nacimiento',
            'relacion_afinidad',
            'bien',
            'tipo_antecedente_conflic',
        ]

class HechoForm(forms.ModelForm):
    class Meta:
        model = Hecho
        fields = [
            'tiempo_violencia',
            'fecha',
            'hora',
            'descripcion_hecho',
            'denuncias',
            'fecha_denuncia',
            'institucion_denuncia',
            'municipio_acontecimiento',
            'tipo_violencia'
        ]

class ReferenciaFamiliarForm(forms.ModelForm):
    class Meta:
        model = ReferenciaFamiliar
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'relacion_afinidad']

class HijoForm(forms.ModelForm):
    class Meta:
        model = Hijo
        fields = ['nombre', 'apellido', 'genero', 'edad', 'es_reconocido', 'es_estudiante', 'establecimiento']


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = [
            'referente', 'hora_ingreso', 'nombre', 'apellido', 'telefono', 'dpi',
            'fecha_nacimiento', 'direccion', 'lectura_escritura', 'profesion',
            'ocupacion', 'direccion_trabajo', 'telefono_trabajo', 'antecedentes_enfermedad',
            'enfermedad', 'presenta_discapacidad', 'discapacidad', 'estado_gestacion',
            'tiempo_gestacion', 'dependencia_adictiva', 'dependencia', 'apoyo_familiar',
            'escolaridad', 'estado_civil', 'estado_vivienda', 'etnia', 'municipio_nacimiento',
            'relacion_afinidad', 'municipio_direccion', 'idioma', 'religion'
        ]
    

    widgets = {
        'referente': forms.TextInput(attrs={'class': 'form-control'}),
        'hora_ingreso': forms.TimeInput(attrs={'class': 'form-control','type': 'time'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        'dpi': forms.TextInput(attrs={'class': 'form-control'}),
        'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'lectura_escritura': forms.CheckboxInput(attrs={'class': 'form-select'}),
        'profesion': forms.TextInput(attrs={'class': 'form-control'}),
        'ocupacion': forms.TextInput(attrs={'class': 'form-control'}),
        'direccion_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
        'telefono_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
        'antecedentes_enfermedad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'enfermedad': forms.TextInput(attrs={'class': 'form-control'}),
        'presenta_discapacidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'discapacidad': forms.TextInput(attrs={'class': 'form-control'}),
        'estado_gestacion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'tiempo_gestacion': forms.TextInput(attrs={'class': 'form-control'}),
        'dependencia_adictiva': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'dependencia': forms.Select(attrs={'class': 'form-select'}),
        'apoyo_familiar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'escolaridad': forms.Select(attrs={'class': 'form-select'}),
        'estado_civil': forms.Select(attrs={'class': 'form-select'}),
        'estado_vivienda': forms.Select(attrs={'class': 'form-select'}),
        'etnia': forms.Select(attrs={'class': 'form-select'}),
        'municipio_nacimiento': forms.Select(attrs={'class': 'form-select'}),
        'relacion_afinidad': forms.Select(attrs={'class': 'form-select'}),
        'municipio_direccion': forms.Select(attrs={'class': 'form-select'}),
        'idioma': forms.Select(attrs={'class': 'form-select'}),
        'religion': forms.Select(attrs={'class': 'form-select'}),
    }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'hora_ingreso' not in self.initial:
            self.fields['hora_ingreso'].initial = timezone.now().strftime('%H:%M')


class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['idioma'] 

