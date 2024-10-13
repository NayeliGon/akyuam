from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import registrar_participante
from .views import registrar_idioma
from .views import registrar_hijo
from .views import referenciaFamiliar
from .views import registrar_hecho
from .views import registrar_agresor
from .views import eliminar_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='sistema/login.html'), name='login'),
    path('home/', views.home_view, name='home'),  
    path('sesiones/',login_required( views.sesiones_view), name='sesiones'),  
    path('emergencias/', login_required(views.emergencias_view), name='emergencias'),  
    path('consulta-asistencia/', login_required(views.consulta_asistencia_view), name='consulta_asistencia'), 
    path('calcular-gastos/', login_required(views.calcular_gastos_view), name='calcular_gastos'),  
    path('administrar-usuarios/', login_required(views.administrar_usuarios_view), name='administrar_usuarios'),  
    path('logout/', views.logout_view, name='logout'),  
    path('boton-emergencia/', views.boton_emergencia_view, name='boton'), 
    path('restablecer-contrasena/<int:user_id>/', views.restablecer_contrasena_view, name='restablecer_contrasena'),
    path('registrar-idioma/', registrar_idioma, name='registrar_idioma'),
    path('registrar-participante/', views.registrar_participante, name='registrar_participante'),
    path('registrar_hijo/<int:participante_id>/', views.registrar_hijo, name='registrar_hijo'),
    path('referencia-familiar/<int:participante_id>/', referenciaFamiliar, name='referencia_familiar'),
    path('registrar-hecho/<int:participante_id>/', registrar_hecho, name='registrar_hecho'),
    path('registrar-agresor/<int:participante_id>/', registrar_agresor, name='registrar_agresor'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('albergue/', views.albergue_view, name='albergue'),
    path('change-password/', views.change_password, name='change_password'),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
]
