import pika

FILA = 'FILA_TESTE'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=FILA)

channel.basic_publish(exchange='',
                      routing_key=FILA,
                      body='Mensagem teste 2')

connection.close()
