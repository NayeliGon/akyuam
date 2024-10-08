from django.shortcuts import render, redirect
from .models import Participante
from .forms import MunicipioForm, DepartamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth import logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
def home_view(request):
    return render(request, 'sistema/home.html')

@login_required
def registrar_participante_view(request):
    grupos_permitidos = ['Administrador', 'Recepcion']
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
     if request.method == 'POST':
       
        n_expediente = request.POST.get('n_expediente')
        n_ingreso = request.POST.get('n_ingreso')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        telefono = request.POST.get('telefono')
        municipio_id = request.POST.get('municipio')  
        departamento_id = request.POST.get('departamento')
        estadocivil_id = request.POST.get('estadocivil')
        profesion_ocupacion = request.POST.get('profesion_ocupacion')
        descripcion_hecho = request.POST.get('descripcion_hecho')
        area_id = request.POST.get('area')

       
        participante = Participante(
            n_expediente=n_expediente,
            n_ingreso=n_ingreso,
            nombre=nombre,
            apellidos=apellidos,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            municipio_id=municipio_id,
            departamento_id=departamento_id,
            estadocivil_id=estadocivil_id,
            profesion_ocupacion=profesion_ocupacion,
            descripcion_hecho=descripcion_hecho,
            area_id=area_id
        )
        participante.save()


        return redirect('/gracias/')  
    
  
     return render(request, 'sistema/registrar_participante.html')
    else:
        return render(request, 'sistema/acceso_denegado.html', status=403)

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
def administrar_usuarios_view(request):
    grupos_permitidos = ['Administrador']
    
    if request.user.groups.filter(name__in=grupos_permitidos).exists():
        if request.method == 'POST':
            # Obtener datos del formulario
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['correo']
            contraseña = request.POST['contraseña']
            nivel_usuario = request.POST['nivel-usuario']

            # Validar el nivel de usuario
            if nivel_usuario == '1':  # Administrador
                grupo = Group.objects.get(name='Administrador')
            elif nivel_usuario == '2':  # Recepcionista
                grupo = Group.objects.get(name='Recepcionista')
            elif nivel_usuario == '3':  # Encargado
                grupo = Group.objects.get(name='Encargado')
            else:
                messages.error(request, 'Por favor, selecciona un nivel de usuario válido.')
                return render(request, 'sistema/administrar_usuarios.html')

            # Crear el usuario
            try:
                user = User.objects.create_user(
                    username=correo,  # Asignar el correo como nombre de usuario
                    email=correo,
                    password=contraseña,
                    first_name=nombre,
                    last_name=apellido
                )
                # Asignar el grupo al usuario
                user.groups.add(grupo)
                user.save()
                messages.success(request, 'Usuario registrado correctamente.')
                return redirect('administrar_usuarios')  # Redirigir a la misma vista después del registro
            except Exception as e:
                messages.error(request, f'Error al registrar el usuario: {e}')
                return render(request, 'sistema/administrar_usuarios.html')
        
        # Si el método no es POST, mostrar la página normalmente
        return render(request, 'sistema/administrar_usuarios.html')

    # Si el usuario no tiene permisos, redirigir a una página de acceso denegado
    return render(request, 'sistema/acceso_denegado.html', status=403)

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
