# Tutorial Three

## *Publish/Subscribe*
### Deliver a message to multiple consumers.


#### Consist in two programs:
 - First will emit log messages
 - Second will receive messages and print them


The main idea in the messaging model in Rabbit is that the producer never sends any messages directly to a queue.
Instead, their producer only send messages to an *exchange*.

The exchange knows exactly what to do with a message it receives:
 - Send to a particular queue;
 - Append to many queues;
 - Discard;

Available types of exchange:
 - direct
 - topic
 - headers
 - fanout

```python
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
```

Publishing to our named exchange:
```python
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
```

Temporary queues
```python
result = channel.queue_declare(queue='')
```

Bindings
```python
channel.queue_bind(exchange='logs',
                   queue=result.method.queue)
```

Dúvidas:
Criou e consumiu as mensagens, mas o comando rabbitmqctl.bat 
não está funcionando no windows.

