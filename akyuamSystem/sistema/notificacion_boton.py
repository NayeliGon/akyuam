import os
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Intentar cargar las variables desde el archivo .env solo en desarrollo
if os.getenv('ENV') != 'production':
    load_dotenv()

# Ahora obtén las variables del entorno, ya sea desde .env o desde las variables del sistema
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

def enviar_mensaje(nombre,apellido,direccion, telefono):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{nombre} {apellido} necesita ayuda, se encuentra en riesgo, su dirección es {direccion}, y su número de telefono es {telefono}",
        from_="+15306658627",
        to="+50251319451",
    )