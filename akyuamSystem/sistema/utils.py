from django.utils import timezone
from .models import Participante

def generar_numero_expediente():
    año_actual = timezone.now().year
    
    ultimo_participante = Participante.objects.filter(no_expediente__endswith=f"-{año_actual}").order_by('-id').first()
    
    if ultimo_participante:
        ultimo_numero = int(ultimo_participante.no_expediente.split('-')[0])
        nuevo_numero = ultimo_numero + 1
    else:
        nuevo_numero = 1
    numero_expediente = f"{nuevo_numero}-{año_actual}"
    
    return numero_expediente
