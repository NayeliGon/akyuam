from django.shortcuts import render, redirect
from .models import TipoViolencia, Departamento, Municipio,Escolaridad,EstadoCivil,EstadoVivienda,Etnia,Idioma,RelacionAfinidad
from .models import Religion, Bienes,TipoAntecedente,Participante,Hijo,Hecho,ReferenciaFamiliar,Agresor
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden

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
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ParticipanteForm  
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from .models import Idioma
from .forms import IdiomaForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import HijoForm
from .models import Participante
from .forms import ReferenciaFamiliarForm
from .forms import HechoForm
from .forms import AgresorForm


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
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save()
            print(f"ID del participante creado: {participante.id}")  
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
            print(f"ID del participante creado: {participante.id}") 
            return redirect('referencia_familiar', participante_id=participante.id)

    else:
        form = HijoForm()
    
    return render(request, 'sistema/registrar_hijo.html', {'form': form, 'participante': participante})


@login_required
def referenciaFamiliar(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    
    if request.method == 'POST':
        form = ReferenciaFamiliarForm(request.POST)
        if form.is_valid():
            referencia_familiar = form.save(commit=False) 
            referencia_familiar.participante_familiar = participante 
            referencia_familiar.save() 
            print(f"ID del participante asociado: {participante.id}") 
            return redirect('registrar_hecho', participante_id=participante.id)
    else:
        form = ReferenciaFamiliarForm()
    
    return render(request, 'sistema/referencia_familiar.html', {'form': form, 'participante': participante})

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
        form = AgresorForm()

    return render(request, 'sistema/registrar_agresor.html', {'form': form, 'participante': participante})

@login_required
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
            hecho.participante = participante  
            hecho.save()
            print(f"ID del hecho creado: {hecho.id}")  
            return redirect('registrar_agresor', participante_id=participante.id)  
    else:
        form = HechoForm()

    return render(request, 'sistema/registrar_hecho.html', {'form': form, 'participante': participante})


@login_required
def home_view(request):
    return render(request, 'sistema/home.html')



@login_required
def sesiones_view(request):
    grupos_permitidos = ['Administrador', 'Encargado']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
     return render(request, 'sistema/registro.html')
    else:
        return render(request, 'sistema/acceso_denegado.html', status=403)

@login_required
def consulta_asistencia_view(request):
    grupos_permitidos = ['Administrador', 'Encargado']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
     return render(request, 'sistema/consulta_asistencia.html')
    else:
        return render(request, 'sistema/acceso_denegado.html', status=403)
    
@login_required
def calcular_gastos_view(request):
    grupos_permitidos = ['Administrador']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
       return render(request, 'sistema/calcular_gastos.html')
    else: 
        return render(request, 'sistema/acceso_denegado.html', status=403)
    



@login_required
def restablecer_contrasena_view(request, user_id):
    grupos_permitidos = ['Administrador']  
    if not request.user.groups.filter(name__in=grupos_permitidos).exists():
        return render(request, 'sistema/acceso_denegado.html', status=403)


    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        contraseña_nueva = request.POST.get('contraseña_nueva')
        confirmar_contraseña = request.POST.get('confirmar_contraseña')

        if contraseña_nueva != confirmar_contraseña:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('restablecer_contrasena', user_id=user.id)


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
       
        user_id = request.POST.get('user_id')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        nivel_usuario = request.POST.get('nivel-usuario')

      
        if nivel_usuario == '1':  # Administrador
            grupo = Group.objects.get(name='Administrador')
        elif nivel_usuario == '2':  # Recepcionista
            grupo = Group.objects.get(name='Recepcionista')
        elif nivel_usuario == '3':  # Encargado
            grupo = Group.objects.get(name='Encargado')
        else:
            messages.error(request, 'Por favor, selecciona un nivel de usuario válido.')
            return redirect('administrar_usuarios')

        if user_id:
            
            user = get_object_or_404(User, id=user_id)
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo
            if contraseña:  
                user.set_password(contraseña)
            user.groups.clear() 
            user.groups.add(grupo)  
            user.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
        else:
           
            try:
                user = User.objects.create_user(
                    username=correo,
                    email=correo,
                    password=contraseña,
                    first_name=nombre,
                    last_name=apellido
                )
                
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
