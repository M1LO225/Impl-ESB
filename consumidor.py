from azure.servicebus import ServiceBusClient

# Reemplaza con tu connection string y nombre de la cola
CONNECTION_STR = "Endpoint=sb://serviceemiliobustests.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=yvTkLsaDN+MWSLAPkoBbFKQIfEIqzEXx2+ASbGIQCjo="
QUEUE_NAME = "incidents"

def recibir_mensajes():
    with ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True) as client:
        receiver = client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=5)
        with receiver:
            for mensaje in receiver:
                print("Mensaje recibido:", str(mensaje))
                receiver.complete_message(mensaje)

# Ejemplo de uso
recibir_mensajes()
