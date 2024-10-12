from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  
    path('sesiones/',login_required( views.sesiones_view), name='sesiones'),  
    path('emergencias/', login_required(views.emergencias_view), name='emergencias'),  
    path('registrar-participante/', login_required(views.registrar_participante_view), name='registrar_participante'), 
    path('consulta-asistencia/', login_required(views.consulta_asistencia_view), name='consulta_asistencia'), 
    path('calcular-gastos/', login_required(views.calcular_gastos_view), name='calcular_gastos'),  
    path('administrar-usuarios/', login_required(views.administrar_usuarios_view), name='administrar_usuarios'),  
    path('logout/', views.logout_view, name='logout'),  
    path('boton-emergencia/', views.boton_emergencia_view, name='boton'), 
    path('enviar-notificacion/', views.envio_boton_view, name='notificacion_emergencia'),

    path('restablecer-contrasena/<int:user_id>/', views.restablecer_contrasena_view, name='restablecer_contrasena'),
]
