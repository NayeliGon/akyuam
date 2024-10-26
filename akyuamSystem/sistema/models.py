from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone



class Idioma(models.Model):
    id_idioma = models.AutoField(primary_key=True)
    idioma = models.CharField(max_length=50)

    def __str__(self):
        return self.idioma


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
    

class EstadoIngreso(models.Model):
    estado_ingreso = models.CharField(max_length=100, null=True, blank=True)


    def _str_(self):
        return self.estado_ingreso  


class Participante(models.Model):
    id = models.AutoField(primary_key=True)
    no_expediente = models.CharField(max_length=50)
    referente = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    hora_ingreso = models.TimeField(null=True, blank=True)  # Opcional
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    dpi = models.CharField(max_length=20,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Opcional
    direccion = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    lectura_escritura = models.BooleanField(default=False)  # Valor por defecto
    profesion = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    ocupacion = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    direccion_trabajo = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    telefono_trabajo = models.CharField(max_length=15, null=True, blank=True)  # Opcional
    antecedentes_enfermedad = models.BooleanField(default=False)  # Valor por defecto
    enfermedad = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    presenta_discapacidad = models.BooleanField(default=False)  # Valor por defecto
    discapacidad = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    estado_gestacion = models.BooleanField(default=False)  # Valor por defecto
    tiempo_gestacion = models.CharField(max_length=15, null=True, blank=True)  # Opcional
    dependencia_adictiva = models.BooleanField(default=False)  # Valor por defecto
    dependencia = models.ForeignKey(DependenciaAdictiva, on_delete=models.CASCADE, null=True, blank=True)  # Opcional
    apoyo_familiar = models.BooleanField(default=False)  # Valor por defecto, opcional
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    estado_vivienda = models.ForeignKey(EstadoVivienda, on_delete=models.CASCADE)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    municipio_nacimiento = models.ForeignKey(Municipio, related_name='nacimiento', on_delete=models.CASCADE)
    relacion_afinidad = models.ForeignKey(RelacionAfinidad, on_delete=models.CASCADE)
    municipio_direccion = models.ForeignKey(Municipio, related_name='direccion', on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE) 

    #campos extra

    fecha_ingreso = models.DateField(null=True, blank=True)  # Opcional
    lugar_ingreso= models.CharField(max_length=15, null=True, blank=True)
    estado_ingreso= models.ForeignKey(EstadoIngreso, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.no_expediente}"


class Hijo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    edad = models.CharField(max_length=10)
    es_reconocido = models.BooleanField()
    es_estudiante = models.BooleanField()
    establecimiento = models.CharField(max_length=100, null=True, blank=True)
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
    tipo_violencia = models.ForeignKey(TipoViolencia, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    municipio_acontecimiento = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    descripcion_hecho = models.TextField()
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    denuncias = models.BooleanField()
    fecha_denuncia = models.DateField(blank=True, null=True)
    institucion_denuncia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Hecho en {self.municipio_acontecimiento} el {self.fecha}"

class Agresor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    dpi = models.CharField(max_length=20, null=True, blank=True)
    etnia = models.ForeignKey(Etnia, on_delete=models.CASCADE)
    municipio_nacimiento = models.ForeignKey(Municipio, related_name='nacimiento_agresor', on_delete=models.CASCADE)
    caracteristicas_fisicas = models.TextField()
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    relacion_afinidad = models.ForeignKey(RelacionAfinidad, on_delete=models.CASCADE)
    lectura_escritura = models.BooleanField()
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    actividad_laboral = models.CharField(max_length=100,blank=True, null= True)
    nombre_lugar_trabajo = models.CharField(max_length=50,blank=True, null= True)
    direccion_trabajo = models.CharField(max_length=100,blank=True, null= True)
    telefono_trabajo = models.CharField(max_length=20,blank=True, null= True)
    ingreso_mensual = models.CharField(max_length=50, blank=True, null= True)
    posee_bienes = models.BooleanField()
    bien = models.ForeignKey(Bienes, on_delete=models.CASCADE,blank=True, null= True)
    otros_bienes = models.TextField(blank=True, null= True)
    antecedentes_conflictividad = models.BooleanField()
    tipo_antecedente_conflic = models.ForeignKey(TipoAntecedente, on_delete=models.CASCADE,blank=True, null= True)
    otros_antecedentes_conflic = models.TextField(blank=True, null= True)
    antecedentes_enfermedad = models.BooleanField()
    descripcion_enfermedad = models.TextField(blank=True, null= True)
    dependencias_adictivas = models.BooleanField()
    dependencia = models.ForeignKey(DependenciaAdictiva, on_delete=models.CASCADE,blank=True, null= True)
    otras_dependencias = models.TextField(blank=True, null= True)
    usa_armas = models.BooleanField()
    descripcion_armas = models.TextField(blank=True, null= True)
    referencias_personales = models.TextField(blank=True, null= True)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



class AreaDeAtencion(models.Model):
    area_atencion = models.CharField(max_length=50)

    def __str__(self):
        return self.area_atencion



class Sesion(models.Model):
    fecha = models.DateField()
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)  
    area_atencion = models.ForeignKey(AreaDeAtencion, on_delete=models.CASCADE)  
    actividad = models.TextField()
    resultados = models.TextField(blank=True, null=True)  # Opcional
    recomendaciones = models.TextField(blank=True, null=True)  # Opcional
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)  

    def __str__(self):
        return f'Sesión {self.id} - {self.fecha}'
    



class Albergue(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(default=timezone.now)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    cantidad_hijos = models.IntegerField()
