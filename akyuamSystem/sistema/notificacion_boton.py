import os
from twilio.rest import Client

def enviar_mensaje(nombre,apellido,direccion):
    account_sid = "AC6ee2435299b4d797d46357cc8420b70b"
    auth_token = "f5985b3a1bdce5b4a59e56ba7be4180a"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"{nombre} {apellido} está sufriendo violencia intrafamiliar, su dirección es {direccion}",
        from_="+18647272971",
        to="+50236313786",
    )