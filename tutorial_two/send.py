import pika, sys

FILA = 'FILA_TESTE'
message = ' '.join(sys.argv[1:]) or 'Hello World'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=FILA)

channel.basic_publish(exchange='',
                      routing_key=FILA,
                      body=message)

print('[x] Enviou %r' % message)

connection.close()
