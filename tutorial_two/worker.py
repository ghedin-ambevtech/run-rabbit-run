import pika, os, sys
import time

FILA = 'FILA_TESTE'

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=FILA)

    def callback(ch, method, properties, body):
        print(f'[x] received {body.decode()}')
        time.sleep(body.count(b'.'))
        print('[x] Done')
        channel.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(
        queue=FILA,
        on_message_callback=callback
    )

    print('[*] Waiting for messages. To exit press Ctrl + C')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

    print('Parei no message durability https://www.rabbitmq.com/tutorials/tutorial-two-python.html ')
    print('duvida do message ack, e sobre como testar ele aqui ')