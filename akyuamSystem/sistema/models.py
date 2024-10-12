from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



class Bienes(models.Model):
    id_bien = models.AutoField(primary_key=True)
    bien = models.CharField(max_length=50)

    def __str__(self):
        return self.bien

class TipoAntecedente(models.Model):
    id_antecedente = models.AutoField(primary_key=True)
    antecedente = models.CharField(max_length=50)

    def __str__(self):
        return self.antecedente


class Etnia(models.Model):
    id_etnia = models.AutoField(primary_key=True)
    etnia = models.CharField(max_length=30)

    def __str__(self):
        return self.etnia

class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(primary_key=True)
    estado_civil = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_civil

class RelacionAfinidad(models.Model):
    id_relacionafinidad = models.AutoField(primary_key=True)
    relacion_afinidad = models.CharField(max_length=50)

    def __str__(self):
        return self.relacion_afinidad

class EstadoVivienda(models.Model):
    id_estado_vivienda = models.AutoField(primary_key=True)
    estado_vivienda = models.CharField(max_length=50)

    def __str__(self):
        return self.estado_vivienda

class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.idioma

class Religion(models.Model):
    id_religion = models.AutoField(primary_key=True)
    religion = models.CharField(max_length=50)

    def __str__(self):
        return self.religion

class Escolaridad(models.Model):
    id_escolaridad = models.AutoField(primary_key=True)
    escolaridad = models.CharField(max_length=50)

    def __str__(self):
        return self.escolaridad

class DependenciaAdictiva(models.Model):
    id_dependencia = models.AutoField(primary_key=True)
    dependencia = models.CharField(max_length=50)

    def __str__(self):
        return self.dependencia

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.genero


class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    id_municipio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class TipoViolencia(models.Model):
    tipo_violencia = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_violencia

class Participante(models.Model):
    no_expediente = models.CharField(max_length=50)
    referente = models.CharField(max_length=100)
    hora_ingreso = models.TimeField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    dpi = models.CharField(max_length=20)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    municipio_nacimiento = models.ForeignKey(Municipio, related_name='nacimiento', on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    relacion_afinidad = models.ForeignKey(RelacionAfinidad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    municipio_direccion = models.ForeignKey(Municipio, related_name='direccion', on_delete=models.CASCADE)
    estado_vivienda = models.ForeignKey(EstadoVivienda, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    lectura_escritura = models.BooleanField()
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE)
    profesion = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    direccion_trabajo = models.CharField(max_length=100)
    telefono_trabajo = models.CharField(max_length=15)
    antecedentes_enfermedad = models.BooleanField()
    enfermedad = models.CharField(max_length=100)
    presenta_discapacidad = models.BooleanField()
    discapacidad = models.CharField(max_length=100)
    estado_gestacion = models.BooleanField()
    tiempo_gestacion = models.CharField(max_length=15)
    dependencia_adictiva = models.BooleanField()
    dependencia = models.ForeignKey(DependenciaAdictiva, on_delete=models.CASCADE)
    apoyo_familiar = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Hijo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    edad = models.CharField(max_length=10)
    es_reconocido = models.BooleanField()
    es_estudiante = models.BooleanField()
    establecimiento = models.CharField(max_length=100)
    participante_madre = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class ReferenciaFamiliar(models.Model):
    relacion_afinidad = models.ForeignKey(RelacionAfinidad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    participante_familiar = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Hecho(models.Model):
    tiempo_violencia = models.CharField(max_length=50)
    tipo_violencia = models.ForeignKey(TipoAntecedente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    municipio_acontecimiento = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    descripcion_hecho = models.TextField()
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    denuncias = models.BooleanField()
    fecha_denuncia = models.DateField()
    institucion_denuncia = models.TextField()

    def __str__(self):
        return f"Hecho en {self.municipio_acontecimiento} el {self.fecha}"

class Agresor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    dpi = models.CharField(max_length=20)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    municipio_nacimiento = models.ForeignKey(Municipio, related_name='nacimiento_agresor', on_delete=models.CASCADE)
    caracteristicas_fisicas = models.TextField()
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    relacion_afinidad = models.ForeignKey(RelacionAfinidad, on_delete=models.CASCADE)
    lectura_escritura = models.BooleanField()
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    actividad_laboral = models.CharField(max_length=100)
    nombre_lugar_trabajo = models.CharField(max_length=50)
    direccion_trabajo = models.CharField(max_length=100)
    telefono_trabajo = models.CharField(max_length=20)
    ingreso_mensual = models.CharField(max_length=50)
    posee_bienes = models.BooleanField()
    bien = models.ForeignKey(Bienes, on_delete=models.CASCADE)
    otros_bienes = models.TextField()
    antecedentes_conflictividad = models.BooleanField()
    tipo_antecedente_conflic = models.ForeignKey(TipoAntecedente, on_delete=models.CASCADE)
    otros_antecedentes_conflic = models.TextField()
    antecedentes_enfermedad = models.BooleanField()
    descripcion_enfermedad = models.TextField()
    dependencias_adictivas = models.BooleanField()
    dependencia = models.ForeignKey(DependenciaAdictiva, on_delete=models.CASCADE)
    otras_dependencias = models.TextField()
    usa_armas = models.BooleanField()
    descripcion_armas = models.TextField()
    referencias_personales = models.TextField()
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    observaciones = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


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


