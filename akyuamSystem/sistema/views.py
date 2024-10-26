from django.shortcuts import render, redirect
from .models import TipoViolencia
from .models import Departamento
from .models import Municipio
from .models import Escolaridad
from .models import EstadoCivil
from .models import EstadoVivienda
from .models import Etnia
from .models import Idioma
from .models import RelacionAfinidad
from .models import Religion
from .models import Bienes
from .models import TipoAntecedente
from .models import Participante
from .models import Hijo
from .models import Hecho
from .models import ReferenciaFamiliar
from .models import Agresor
from .models import Sesion
from .models import Albergue
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Participante
from .forms import ParticipanteForm  
from .utils import generar_numero_expediente  
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from . import notificacion_boton
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ParticipanteForm  # Asegúrate de que este import sea correcto
from .models import Municipio, Escolaridad, EstadoCivil, EstadoVivienda, Etnia, Idioma, RelacionAfinidad, Religion
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Participante  # Asegúrate de tener tu modelo 'Participante' definido
from django.contrib import messages
from .forms import EditarPerfilForm
from django.contrib.auth import update_session_auth_hash
from .models import Idioma
from .forms import IdiomaForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HijoForm
from .forms import HijoExtraForm
from .models import Participante
from .forms import ReferenciaFamiliarForm
from .forms import ReferenciaFamiliarExtraForm
from .forms import HechoForm
from .forms import AgresorForm
from .forms import SesionForm
from .forms import FechaRangoForm
from .forms import FechaRangoAsistenciaForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .models import Participante
from django.utils import timezone
from django.db.models import Count, OuterRef, Subquery
# views.py

from django.shortcuts import render
from django.db.models import F, ExpressionWrapper, fields
from .models import Albergue
from .forms import FechaRangoForm
from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Participante

# Función para convertir HTML a PDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pdf = pisa.CreatePDF(html, dest=result)
    if not pdf.err:
        return result
    return None

# Vista para generar el PDF
@login_required
def participante_pdf(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    hijos = participante.hijo_set.all()
    referencias = participante.referenciafamiliar_set.all()
    hechos = participante.hecho_set.all()
    agresor = participante.agresor_set.first()

    context = {
        'participante': participante,
        'hijos': hijos,
        'referencias': referencias,
        'hechos': hechos,
        'agresor': agresor,
    }
    
    pdf = render_to_pdf('sistema/participante_pdf.html', context)
    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse("Error al generar el PDF", status=400)


@login_required
def buscar_participante_albergue(request):
    grupos_permitidos = ['Administrador']

    # Verificar si el usuario pertenece a los grupos permitidos
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)
    form = FechaRangoForm()
    resultados = []
    total_comidas = 0
    costo_total = 0

    if request.method == 'GET':
        form = FechaRangoForm(request.GET)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            costo_por_comida = form.cleaned_data['costo_por_comida']

            # Filtrar los resultados en base a las fechas
            resultados = Albergue.objects.filter(
                fecha_ingreso__gte=fecha_inicio,
                fecha_salida__lte=fecha_fin
            )

            for resultado in resultados:
                # Calcular el número de días en el albergue
                resultado.dias_en_albergue = (resultado.fecha_salida - resultado.fecha_ingreso).days + 1

                # Calcular la cantidad de personas (participante + hijos)
                total_personas = 1 + resultado.cantidad_hijos  # 1 por la participante

                # Calcular el costo total para la participante y sus hijos
                resultado.costo_gastado = resultado.dias_en_albergue * 5 * total_personas * costo_por_comida

            # Sumar los costos de todos los resultados
            costo_total = sum([res.costo_gastado for res in resultados])

    return render(request, 'sistema/calcular_gastos.html', {
        'form': form,
        'resultados': resultados,
        'costo_total': costo_total
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            logout(request)
            messages.success(request, 'Tu contraseña ha sido cambiada exitosamente. Por favor, inicia sesión de nuevo.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'sistema/perfil.html', {
        'password_form': form,
    })





@login_required
def perfil_view(request):
    usuario = request.user

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil')
        elif password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Mantiene al usuario logueado
            messages.success(request, 'Tu contraseña ha sido actualizada.')
            return redirect('login')
    else:
        form = EditarPerfilForm(instance=usuario)
        password_form = PasswordChangeForm(user=request.user)

    return render(request, 'sistema/perfil.html', {'form': form, 'password_form': password_form})


@login_required
def albergue_view(request):
    
    return render(request, 'sistema/albergue.html')

@login_required
def registrar_idioma(request):
    if request.method == 'POST':
        form = IdiomaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('sistema/registrar_idioma.html')  
    else:
        form = IdiomaForm()  

    context = {
        'form': form,
    }
    return render(request, 'sistema/registrar_idioma.html', context)

@login_required
def registrar_participante(request):
    grupos_permitidos = ['Administrador', 'Recepcion']

    # Verificar si el usuario pertenece a los grupos permitidos
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save()
            print(f"ID del participante creado: {participante.id}")  # Verifica el ID en la consola
            return redirect('registrar_hijo', participante_id=participante.id)
    else:
        form = ParticipanteForm()
    return render(request, 'sistema/registrar_participante.html', {'form': form})

@login_required
def registrar_hijo(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        form = HijoForm(request.POST)
        if form.is_valid():
            hijo = form.save(commit=False)
            hijo.participante_madre = participante
            hijo.save()
            print(f"ID del participante creado: {participante.id}")  # Verifica el ID en la consola
            return redirect('referencia_familiar', participante_id=participante.id)

    else:
        form = HijoForm()
    
    return render(request, 'sistema/registrar_hijo.html', {'form': form, 'participante': participante})



#Registrar hijos extra (aparte del que se registra con la partipante al principio)
@login_required
def registrar_hijo_extra_view(request):
    if request.method == 'POST':
        form = HijoExtraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_participante')
    else:
        form = HijoExtraForm()
    return render(request, 'sistema/registrar_hijo_extra.html', {'form': form})



#Registrar familiar extra (aparte del que se registra con la partipante al principio)
@login_required
def registrar_familiar_extra_view(request):
    if request.method == 'POST':
        form = ReferenciaFamiliarExtraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_participante')
    else:
        form = ReferenciaFamiliarExtraForm()
    return render(request, 'sistema/registrar_familiar_extra.html', {'form': form})




#Omitir registro de hijos
@login_required
def no_registrar_hijo(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        return redirect('referencia_familiar', participante_id=participante.id)



@login_required
def referenciaFamiliar(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        form = ReferenciaFamiliarForm(request.POST)
        if form.is_valid():
            referencia_familiar = form.save(commit=False) 
            referencia_familiar.participante_familiar = participante  
            referencia_familiar.save()  # Guardar en la base de datos
            print(f"ID del participante asociado: {participante.id}") 
            return redirect('registrar_hecho', participante_id=participante.id)  
    else:
        form = ReferenciaFamiliarForm()
    
    return render(request, 'sistema/referencia_familiar.html', {'form': form, 'participante': participante})



@login_required
def omitir_referenciaFamiliar(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        return redirect('registrar_hecho', participante_id=participante.id)




@login_required
def registrar_agresor(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    if request.method == 'POST':
        form = AgresorForm(request.POST)
        if form.is_valid():
            agresor = form.save(commit=False)
            agresor.participante = participante  
            agresor.save()
            return redirect('home') 
        else:
            print(form.errors)  
    else:
        form = AgresorForm()

    return render(request, 'sistema/registrar_agresor.html', {'form': form, 'participante': participante})

#@login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'sistema/login.html')

@login_required
def registrar_hecho(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    if request.method == 'POST':
        form = HechoForm(request.POST)
        if form.is_valid():
            hecho = form.save(commit=False)
            hecho.participante = participante  # Asociar el participante
            hecho.save()
            print(f"ID del hecho creado: {hecho.id}")  # Verifica el ID en la consola
            return redirect('registrar_agresor', participante_id=participante.id)  # Redirige a la vista deseada con el ID del participante
    else:
        form = HechoForm()

    return render(request, 'sistema/registrar_hecho.html', {'form': form, 'participante': participante})




@login_required
def omitir_registrar_hecho(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    if request.method == 'POST':
        return redirect('registrar_agresor', participante_id=participante.id)





@login_required
def home_view(request):
    return render(request, 'sistema/home.html')



@login_required
def sesiones_view(request):
    grupos_permitidos = ['Administrador', 'Encargado']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
        if request.method == 'GET':
            participantes = Participante.objects.values('id', 'nombre', 'apellido', 'direccion', 'dpi', 'telefono').order_by('id')
            return render(request, 'sistema/sesiones_participantes.html',{'participantes':participantes})
    else:
        return render(request, 'sistema/acceso_denegado.html', status=403)




@login_required
def consulta_asistencia_view(request):
    grupos_permitidos = ['Administrador', 'Encargado']

    # Verificar si el usuario pertenece a los grupos permitidos
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)

    participantes = []  # Inicializa la lista vacía para evitar mostrar participantes inicialmente

    search = request.POST.get('search', '')

    if request.method == 'POST' and search:
        # Si se realiza una búsqueda, filtra los participantes
        participantes = Participante.objects.filter(
            nombre__icontains=search
        ) | Participante.objects.filter(apellido__icontains=search) | Participante.objects.filter(no_expediente__icontains=search)

    # Preparar el contexto para renderizar la vista
    context = {'participantes': participantes}

    # Renderizar la plantilla con el contexto
    return render(request, 'sistema/calcular_asistencias.html', context)

    
@login_required
def fecha_asistencia_view(request,participante_id):
    participante_obtenida = get_object_or_404(Participante, id=participante_id)

    form = FechaRangoAsistenciaForm()
    resultados = []
    total_resultados = 0
    

    if request.method == 'GET':
        form = FechaRangoAsistenciaForm(request.GET)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            
            
            # Filtrar los resultados en base a las fechas
            resultados = Sesion.objects.filter(
            fecha__gte=fecha_inicio,  # Fecha mayor o igual a la de inicio
            fecha__lte=fecha_fin,      # Fecha menor o igual a la de fin
            participante=participante_obtenida 
            )

            total_resultados = resultados.count()

    context = {
        'form': form,
        'resultados': resultados,
        'participante': participante_obtenida,
        'total_resultados': total_resultados
    }
    
    return render(request, 'sistema/calcular_asistencias2.html', context)








    
@login_required
def calcular_gastos_view(request):
    grupos_permitidos = ['Administrador']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
       return render(request, 'sistema/calcular_gastos.html')
    else: 
        return render(request, 'sistema/acceso_denegado.html', status=403)
    



@login_required
def restablecer_contrasena_view(request, user_id):
    grupos_permitidos = ['Administrador']  # O el grupo que desees
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)

    # Obtener el usuario cuyo password se desea restablecer
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        contraseña_nueva = request.POST.get('contraseña_nueva')
        confirmar_contraseña = request.POST.get('confirmar_contraseña')

        # Validar que las contraseñas coincidan
        if contraseña_nueva != confirmar_contraseña:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('restablecer_contrasena', user_id=user.id)

        # Si las contraseñas coinciden, actualizar la contraseña
        user.set_password(contraseña_nueva)
        user.save()

        messages.success(request, 'Contraseña restablecida exitosamente.')
        return redirect('administrar_usuarios')

    return render(request, 'sistema/restablecer_contrasena.html', {'user': user})


@login_required
def administrar_usuarios_view(request):
    grupos_permitidos = ['Administrador']
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)

    if request.method == 'POST':
        # Obtener datos del formulario
        user_id = request.POST.get('user_id')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        nivel_usuario = request.POST.get('nivel-usuario')

        # Validar el nivel de usuario y asignar grupo
        if nivel_usuario == '1':  # Administrador
            grupo = Group.objects.get(name='Administrador')
        elif nivel_usuario == '2':  # Recepcionista
            grupo = Group.objects.get(name='Recepcion')
        elif nivel_usuario == '3':  # Encargado
            grupo = Group.objects.get(name='Encargado')
        else:
            messages.error(request, 'Por favor, selecciona un nivel de usuario válido.')
            return redirect('administrar_usuarios')

        if user_id:
            # Actualizar usuario existente
            user = get_object_or_404(User, id=user_id)
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo
            if contraseña:  # Solo actualizar contraseña si se ha proporcionado
                user.set_password(contraseña)
            user.groups.clear()  # Limpiar los grupos actuales
            user.groups.add(grupo)  # Asignar el nuevo grupo
            user.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
        else:
            # Crear nuevo usuario
            try:
                user = User.objects.create_user(
                    username=correo,
                    email=correo,
                    password=contraseña,
                    first_name=nombre,
                    last_name=apellido
                )
                # Asignar el grupo al nuevo usuario
                user.groups.add(grupo)
                user.save()
                messages.success(request, 'Usuario registrado exitosamente.')
            except Exception as e:
                messages.error(request, f'Ocurrió un error al registrar el usuario: {e}')
                return redirect('administrar_usuarios')

        return redirect('administrar_usuarios')

    # Listar usuarios
    usuarios = User.objects.all()
    user_to_edit = None
    if request.GET.get('edit_user_id'):
        user_to_edit = get_object_or_404(User, id=request.GET['edit_user_id'])

    return render(request, 'sistema/administrar_usuarios.html', {'usuarios': usuarios, 'user_to_edit': user_to_edit})

@login_required
def eliminar_usuario(request, user_id):
    grupos_permitidos = ['Administrador']
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)

    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('administrar_usuarios')



@login_required
def emergencias_view(request):
    grupos_permitidos = ['Recepcion', 'Administrador']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/emergencias.html')
    else:
        return render(request, 'sistema/acceso_denegado.html', status=403)



def boton_emergencia_view(request):
    return render(request, 'sistema/boton_emergencia.html')


def logout_view(request):

    if 'datos' in request.session:
        del request.session['datos']
    
    logout(request)
    request.session.flush()

    return redirect('login')


#Vista para manejar el envío de datos del boton de emergencia


def envio_boton_view(request):
    
    
    if request.method == 'POST':

        #obtener codigo
        data = json.loads(request.body)
        codigo= data.get('codigo')

        if not codigo:
            return HttpResponse('El código es obligatorio.')

        #consultar existencia de código en la base de datos

        try:

            participante = Participante.objects.filter(no_expediente=codigo).first()

            if not participante:
                return HttpResponse('El código no es válido')
        
            nombre = participante.nombre
            apellido= participante.apellido
            direccion = participante.direccion
            telefono= participante.telefono


    
            print('Datos obtenidos',nombre,apellido, direccion, telefono)
            notificacion_boton.enviar_mensaje(nombre,apellido,direccion, telefono)  # Funcion para enviar mensajes
            return HttpResponse('Mensaje enviado')


        except Participante.DoesNotExist:
            print("No es participante de akyuam")
            return HttpResponse('El código no es válido')
    
       
    else:
        return HttpResponse('Solicitud inválida', status=400)


#Vista para listar las participantes
@login_required
def listar_participantes_view(request):
    if request.method == 'GET':
        participantes = Participante.objects.values('id', 'no_expediente','nombre', 'apellido','direccion', 'dpi', 'telefono').order_by('id')  # Solo los campos necesarios
        return render(request, 'sistema/lista_participantes.html', {'participantes': participantes})


#Actualizar datos generales de la participante
@login_required
def actualizar_participante_view(request, id):
    participante = get_object_or_404(Participante, id=id)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('participantes_lista')  # Redirige a la lista de participantes
    else:
        form = ParticipanteForm(instance=participante)
    
    return render(request, 'sistema/actualizar_participante.html', {'form': form})



#Listar hijos de participante
@login_required
def hijos_participante_view(request, participante_id):
    # Obtener la participante
    participante = get_object_or_404(Participante, id=participante_id)
    # Obtener los hijos asociados a la participante
    hijos = Hijo.objects.filter(participante_madre=participante)
    
    return render(request, 'sistema/actualizar_hijos.html', {'hijos':hijos})





#Actualizar datos de hijos de la participante

@login_required
def actualizar_hijo_view(request, hijo_id):
    # Obtener el participante
    hijo = get_object_or_404(Hijo, id=hijo_id)
     
    if request.method == 'POST':
        form = HijoForm(request.POST, instance=hijo)
        if form.is_valid():
            form.save()
            return redirect('participantes_lista')
    else:
        form = HijoForm(instance=hijo)
    
    return render(request, 'sistema/actualizar_hijo.html', {'form': form})




@login_required
def listar_familiares_view(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    try:
        familiares = ReferenciaFamiliar.objects.filter(participante_familiar=participante)
    except ReferenciaFamiliar.DoesNotExist:
        print('El familiar no existe')

    return render(request, 'sistema/lista-familiares.html', {'familiares':familiares})



#Mostrar formulario para actualizar familiar de participante

@login_required
def actualizar_familiar_view(request, familiar_id):
     

    try:
        familiar = ReferenciaFamiliar.objects.get(id=familiar_id)
    except ReferenciaFamiliar.DoesNotExist:
        print('El familiar no existe')

    if request.method == 'POST':
        form = ReferenciaFamiliarForm(request.POST, instance=familiar)
        if form.is_valid():
            form.save()
            return redirect('participantes_lista')
    else:
        form = ReferenciaFamiliarForm(instance=familiar)
    
    return render(request, 'sistema/actualizar_familiar.html', {'form': form})



#obtener la lista de hechos
@login_required
def listar_hechos_view(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    try:
        hechos = Hecho.objects.filter(participante=participante)
    except Hecho.DoesNotExist:
        print('El familiar no existe')

    return render(request, 'sistema/lista-hechos.html', {'hechos':hechos})



#Mostrar formulario para actualizar hecho de participante

@login_required
def actualizar_hecho_view(request, hecho_id):
     

    try:
        hecho = Hecho.objects.get(id=hecho_id)
    except Hecho.DoesNotExist:
        print('El Hecho no existe')

    if request.method == 'POST':
        form = HechoForm(request.POST, instance=hecho)
        if form.is_valid():
            form.save()
            return redirect('participantes_lista')
    else:
        form = HechoForm(instance=hecho)
    
    return render(request, 'sistema/actualizar_hecho.html', {'form': form})



#obtener la lista de agresores
@login_required
def listar_agresores_view(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    try:
        agresores = Agresor.objects.filter(participante=participante)
    except Agresor.DoesNotExist:
        print('El familiar no existe')

    return render(request, 'sistema/lista_agresores.html', {'agresores':agresores})


#Mostrar formulario para actualizar agresor de participante

@login_required
def actualizar_agresor_view(request, agresor_id):
     

    try:
        agresor = Agresor.objects.get(id=agresor_id)
    except Agresor.DoesNotExist:
        print('El agresor no existe')

    if request.method == 'POST':
        form = AgresorForm(request.POST, instance=agresor)
        if form.is_valid():
            form.save()
            return redirect('participantes_lista')
    else:
        form = AgresorForm(instance=agresor)
    
    return render(request, 'sistema/actualizar_agresor.html', {'form': form})


#Regitrar sesion de una participante
@login_required
def registrar_sesion_view(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        form = SesionForm(request.POST)
        if form.is_valid():
            sesion = form.save(commit=False)
            sesion.participante = participante
            sesion.save()
            return redirect('sesiones')

    else:
        form = SesionForm()
    
    return render(request, 'sistema/registrar_sesion_participantes.html', {'form': form, 'participante': participante})


#Listar todas las sesiones de una participante en específico

@login_required
def lista_sesiones_view(request, participante_id):
    participante_obtenida = get_object_or_404(Participante, id=participante_id)

    sesiones = Sesion.objects.filter(participante=participante_obtenida)
    
    return render(request, 'sistema/lista-sesiones.html', {'sesiones': sesiones})



@login_required
def actualizar_sesion_view(request, sesion_id):
    sesion = Sesion.objects.get(id=sesion_id)
    
    if request.method == 'POST':
        form = SesionForm(request.POST, instance=sesion)
        if form.is_valid():
            sesion = form.save(commit=False)
            sesion.save()
            return redirect('sesiones')

    else:
        form = SesionForm(instance=sesion)
    
    return render(request, 'sistema/actualizar_sesion.html', {'form': form})
    return render(request, 'sistema/registrar_sesion_participantes.html', {'form': form})

@login_required
def buscar_participantes(request):
    query = request.GET.get('query', '').strip()

    # Obtener el último albergue de cada participante
    ultimo_albergue = Albergue.objects.filter(participante=OuterRef('pk')).order_by('-fecha_ingreso')

    if query:
        participantes = Participante.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(no_expediente__icontains=query)
        ).annotate(
            cantidad_hijos=Count('hijo'),
            hijos_albergue=Subquery(ultimo_albergue.values('cantidad_hijos')[:1]),
            ultimo_fecha_ingreso=Subquery(ultimo_albergue.values('fecha_ingreso')[:1]),
            ultimo_fecha_salida=Subquery(ultimo_albergue.values('fecha_salida')[:1])
        )
    else:
        participantes = None

    return render(request, 'sistema/albergue.html', {'participantes': participantes})
@login_required
def ingresar_participante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    if request.method == 'POST':
        fecha_ingreso = request.POST.get('fecha_ingreso')
        cantidad_hijos = request.POST.get('cantidad_hijos')

        nuevo_registro = Albergue(
            participante=participante,
            fecha_ingreso=fecha_ingreso,
            cantidad_hijos=cantidad_hijos
        )
        nuevo_registro.save()

        return redirect('buscar_participantes') 
    return render(request, 'sistema/albergue.html', {'participante': participante})
@login_required
def registrar_salida(request, id_participante):

    participante = get_object_or_404(Participante, id=id_participante)

    if request.method == 'POST':

        fecha_salida = request.POST.get('fecha_salida')

        albergue = get_object_or_404(Albergue, participante=participante)


        albergue.fecha_salida = fecha_salida
        albergue.save()


        return redirect('buscar_participantes')  

    return render(request, 'sistema/albergue.html', {'participante': participante})


