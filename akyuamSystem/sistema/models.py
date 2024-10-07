from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class EstadoCivil(models.Model):
    estadocivil = models.CharField(max_length=50)

class Area(models.Model):
    area = models.CharField(max_length=100)

class Participante(models.Model):
    n_expediente = models.CharField(max_length=50)
    n_ingreso = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    estadocivil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    telefono_trabajo = models.CharField(max_length=20, null=True, blank=True)
    direccion_trabajo = models.CharField(max_length=255, null=True, blank=True)
    profesion_ocupacion = models.CharField(max_length=100)
    albergue = models.BooleanField(default=False)
    enfermedad = models.BooleanField(default=False)
    vivienda = models.BooleanField(default=False)
    dependencias = models.BooleanField(default=False)
    gestacion = models.BooleanField(default=False)
    descripcion_hecho = models.TextField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


'''
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Correo", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
'''


