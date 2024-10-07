from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':

#username = request.POST['username']
#       password = request.POST['password']
 #       user = authenticate(request, username=username, password=password)
 #       if user is not None:
  #          auth_login(request, user)  
  #          return redirect('home')  
  #      else:
 #           messages.error(request, 'Usuario o contraseña incorrectos.')
 #   return render(request, 'sistema/login.html'

        return redirect('home')  
    return render(request, 'sistema/login.html')


def home_view(request):
    return render(request, 'sistema/home.html')


def registrar_participante_view(request):
    return render(request, 'sistema/registrar_participante.html')


def sesiones_view(request):
    return render(request, 'sistema/sesiones.html')


def consulta_asistencia_view(request):
    return render(request, 'sistema/consulta_asistencia.html')


def calcular_gastos_view(request):
    return render(request, 'sistema/calcular_gastos.html')


def administrar_usuarios_view(request):
    return render(request, 'sistema/administrar_usuarios.html')


def emergencias_view(request):
    return render(request, 'sistema/emergencias.html')


def boton_emergencia_view(request):
    return render(request, 'sistema/boton_emergencia.html')


def logout_view(request):
    
    return redirect('login')
