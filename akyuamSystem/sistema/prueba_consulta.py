
from sistema.models import Participante

id_participante = 1


try:

    participante = Participante.objects.get(id=id_participante)
    nombre = participante.nombre
    direccion = participante.direccion
    
    print('Datos obtenidos',nombre, direccion)


except Participante.DoesNotExist:
    print("No es participante de akyuam")