from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
       
        return redirect('home')  
        
    return render(request, 'sistema/login.html')  


'''
 username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'sistema/login.html'


'''

def home_view(request):
    return render(request, 'sistema/home.html')  

from django.shortcuts import render


def emergencias_view(request):
    return render(request, 'sistema/emergencias.html')

def sesiones_view(request):
    return render(request, 'sistema/sesiones.html')
