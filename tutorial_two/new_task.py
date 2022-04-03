import pika, sys

# Mudando de fila no send e na worker
FILA = 'task_queues'
message = ' '.join(sys.argv[1:]) or 'Hello World'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue=FILA)
# adicionando persistencia da mensagem em caso de receiver fora
# channel.queue_declare(queue=FILA, durable=True) ### não achei encontrei o motivo de não funcionar com esse parametro
# retorna 406
channel.queue_declare(queue=FILA)

# adicionando a propriedade de persistencia
channel.basic_publish(exchange='',
                      routing_key=FILA,
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print('[x] Enviou %r' % message)

connection.close()
