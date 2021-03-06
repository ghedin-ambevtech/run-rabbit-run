import pika, os, sys

FILA = 'FILA_TESTE'

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=FILA)

    def callback(ch, method, properties, body):
        print(f'[x] received {body}')

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
