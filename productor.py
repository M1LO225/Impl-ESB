from azure.servicebus import ServiceBusClient, ServiceBusMessage

# Reemplaza con tu connection string y nombre de la cola
CONNECTION_STR = "Endpoint=sb://serviceemiliobustests.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=yvTkLsaDN+MWSLAPkoBbFKQIfEIqzEXx2+ASbGIQCjo="
QUEUE_NAME = "incidents"

def enviar_mensaje(texto):
    with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True) as client:
        sender = client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            mensaje = ServiceBusMessage(texto)
            sender.send_messages(mensaje)
            print("Mensaje enviado:", texto)

# Ejemplo de uso
enviar_mensaje("Hola desde el productor Python!")
