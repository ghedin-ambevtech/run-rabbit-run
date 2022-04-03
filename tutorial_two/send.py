import pika, sys

# Mudando de fila no send e na worker
FILA = 'task_queue'
message = ' '.join(sys.argv[1:]) or 'Hello World'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue=FILA)
# adicionando persistencia da mensagem em caso de receiver fora
channel.queue_declare(queue=FILA, durable=True)

# adicionando a propriedade de persistencia
channel.basic_publish(exchange='',
                      routing_key=FILA,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print('[x] Enviou %r' % message)

connection.close()
