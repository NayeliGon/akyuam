from django.contrib import admin
from django.urls import path, include
from sistema import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  
    path('sistema/', include('sistema.urls')),  
]
