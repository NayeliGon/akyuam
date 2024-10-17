from django import forms
from .models import Participante
from .models import Idioma
from .models import Hijo
from .models import ReferenciaFamiliar
from .models import Hecho
from .models import Agresor
from .models import Sesion
from .models import Albergue
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
        fields = [ 'username']
        widgets = {
            #'email': forms.EmailInput(attrs={'placeholder': 'Correo', 'class': 'editable', 'disabled': 'disabled'}),
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
        exclude= ['participante']  # Excluir el campo 'participante' del formulario
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'dpi': forms.TextInput(attrs={'class': 'form-control'}),
            'etnia': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'municipio_nacimiento': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'caracteristicas_fisicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'relacion_afinidad': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'lectura_escritura': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'escolaridad': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'actividad_laboral': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_lugar_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_trabajo': forms.TextInput(attrs={'class': 'form-control'}),
            'ingreso_mensual': forms.TextInput(attrs={'class': 'form-control'}),
            'posee_bienes': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'bien': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'otros_bienes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'antecedentes_conflictividad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'tipo_antecedente_conflic': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'otros_antecedentes_conflic': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'antecedentes_enfermedad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'descripcion_enfermedad': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dependencias_adictivas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'dependencia': forms.Select(attrs={'class': 'form-select'}),  # Select para ForeignKey
            'otras_dependencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'usa_armas': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Checkbox para BooleanField
            'descripcion_armas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'referencias_personales': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(AgresorForm, self).__init__(*args, **kwargs)
        self.fields['dpi'].required = False
        self.fields['actividad_laboral'].required = False
        self.fields['nombre_lugar_trabajo'].required = False
        self.fields['direccion_trabajo'].required = False
        self.fields['telefono_trabajo'].required = False
        self.fields['ingreso_mensual'].required = False
        self.fields['otros_bienes'].required = False
        self.fields['tipo_antecedente_conflic'].required = False
        self.fields['otros_antecedentes_conflic'].required = False
        self.fields['descripcion_enfermedad'].required = False
        self.fields['dependencia'].required = False
        self.fields['otras_dependencias'].required = False
        self.fields['descripcion_armas'].required = False
        self.fields['referencias_personales'].required = False
        self.fields['observaciones'].required = False

class HechoForm(forms.ModelForm):
    class Meta:
        model = Hecho
        fields = [
            'tiempo_violencia',
            'tipo_violencia',
            'fecha',
            'hora',
            'municipio_acontecimiento',
            'descripcion_hecho',
            'denuncias',
            'fecha_denuncia',
            'institucion_denuncia',
            
           
        ]
        widgets = {
            'tiempo_violencia': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_violencia': forms.Select(attrs={'class': 'form-select'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'municipio_acontecimiento': forms.Select(attrs={'class': 'form-select'}),
            'descripcion_hecho': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'denuncias': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_denuncia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'institucion_denuncia': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(HechoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_denuncia'].required = False
        self.fields['institucion_denuncia'].required = False

class ReferenciaFamiliarForm(forms.ModelForm):
    class Meta:
        model = ReferenciaFamiliar
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'relacion_afinidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'relacion_afinidad': forms.Select(attrs={'class': 'form-select'}),
        }



class ReferenciaFamiliarExtraForm(forms.ModelForm):
    class Meta:
        model = ReferenciaFamiliar
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'relacion_afinidad','participante_familiar']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'relacion_afinidad': forms.Select(attrs={'class': 'form-select'}),
            'participante_familiar': forms.Select(attrs={'class': 'form-select'}),
        }        

class HijoForm(forms.ModelForm):
    class Meta:
        model = Hijo
        fields = ['nombre', 'apellido', 'genero', 'edad', 'es_reconocido', 'es_estudiante', 'establecimiento']
    

    def __init__(self, *args, **kwargs):
        super(HijoForm, self).__init__(*args, **kwargs)

        checkbox_fields = [
            'es_reconocido', 'es_estudiante'
        ]

        for field in checkbox_fields:
            self.fields[field].help_text = 'Marque si la respuesta es "Sí".'

        self.fields['establecimiento'].required = False



class HijoExtraForm(forms.ModelForm):
    class Meta:
        model = Hijo
        fields = ['nombre', 'apellido', 'genero', 'edad', 'es_reconocido', 'es_estudiante', 'establecimiento','participante_madre']
    

    def __init__(self, *args, **kwargs):
        super(HijoExtraForm, self).__init__(*args, **kwargs)
        self.fields['establecimiento'].required = False




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
            'lectura_escritura': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
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
        

     # Modificando campos para que sean opcionales
    def __init__(self, *args, **kwargs):
        super(ParticipanteForm, self).__init__(*args, **kwargs)
        checkbox_fields = [
            'lectura_escritura', 'antecedentes_enfermedad', 'presenta_discapacidad', 
            'estado_gestacion', 'dependencia_adictiva', 'apoyo_familiar'
        ]

        for field in checkbox_fields:
            self.fields[field].help_text = 'Marque si la respuesta es "Sí".'

        self.fields['dpi'].required = False
        self.fields['profesion'].required = False
        self.fields['ocupacion'].required = False
        self.fields['direccion_trabajo'].required = False
        self.fields['telefono_trabajo'].required = False
        self.fields['enfermedad'].required = False
        self.fields['discapacidad'].required = False
        self.fields['tiempo_gestacion'].required = False
        self.fields['dependencia'].required = False
        self.fields['tiempo_gestacion'].required = False
        self.fields['tiempo_gestacion'].required = False
        self.fields['tiempo_gestacion'].required = False

        if 'hora_ingreso' not in self.initial:
            self.fields['hora_ingreso'].initial = timezone.now().strftime('%H:%M')

   
class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['idioma'] 


class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['fecha', 'municipio', 'area_atencion', 'actividad', 'resultados','recomendaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'municipio': forms.Select(attrs={'class': 'form-select'}),
            'area_atencion': forms.Select(attrs={'class': 'form-select'}),
            'actividad': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'resultados': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'recomendaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=True)

class BuscarParticipanteForm(forms.Form):
    nombre = forms.CharField(required=False, label='Nombre')
    apellido = forms.CharField(required=False, label='Apellido')
    numero_expediente = forms.CharField(required=False, label='Número de Expediente')        


class RegistroAlbergueForm(forms.Form):
    fecha_ingreso = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Fecha de ingreso"
    )
    cantidad_hijos = forms.IntegerField(
        min_value=0,
        label="Cantidad de hijos"
    )

class RegistroAlbergueForm(forms.ModelForm):
    class Meta:
        model = Albergue
        fields = ['participante', 'cantidad_hijos']

class RegistroSalidaForm(forms.ModelForm):
    fecha_salida = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Fecha y hora de salida"
    )

    class Meta:
        model = Albergue
        fields = ['fecha_salida']


class FechaRangoForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Selecciona la fecha de inicio'
        }),
        label="Fecha de inicio"
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Selecciona la fecha de fin'
        }),
        label="Fecha de fin"
    )
    costo_por_comida = forms.DecimalField(
        max_digits=10, 
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Costo por comida'
        }),
        label="Costo por comida"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Aplicar clase Bootstrap a todos los campos
