# Tutorial Four
## Routing

Filter only critical error messages to log.

*Binding is a relationship between an exchange and a queue*

````python
channel.queue_bind(exchange=exchange_name,
                   queue=queue_name,
                   routing_key='black')
````

````python
channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
````

````python
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
````


````python
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)
````

