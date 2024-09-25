from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Ruta para login
    path('home/', views.home_view, name='home'), 
    path('sesiones/', views.home_view, name='sesiones'),
]
