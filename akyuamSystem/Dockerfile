# Usamos una imagen ligera de Python
FROM python:3.12.1

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . /app/

# Exponer el puerto para el servidor de Django
EXPOSE 8000

# Comando por defecto para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
