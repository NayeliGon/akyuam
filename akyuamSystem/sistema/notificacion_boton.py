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

def enviar_mensaje(nombre,apellido,direccion):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{nombre} {apellido} está sufriendo violencia intrafamiliar, su dirección es {direccion}",
        from_="+18647272971",
        to="+50236313786",
    )