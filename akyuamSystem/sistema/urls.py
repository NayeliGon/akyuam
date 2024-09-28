from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  
    path('home/', views.home_view, name='home'),  
    path('sesiones/', views.sesiones_view, name='sesiones'),  
    path('emergencias/', views.emergencias_view, name='emergencias'),  
    path('registrar-participante/', views.registrar_participante_view, name='registrar_participante'), 
    path('consulta-asistencia/', views.consulta_asistencia_view, name='consulta_asistencia'), 
    path('calcular-gastos/', views.calcular_gastos_view, name='calcular_gastos'),  
    path('administrar-usuarios/', views.administrar_usuarios_view, name='administrar_usuarios'),  
    path('logout/', views.logout_view, name='logout'),  
]
