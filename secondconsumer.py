import pika
from pika.exchange_type import ExchangeType


def on_message_received(ch, method, properties, body):
    print(f"Second consumer is receiving the message: {body}")

connection_parameters= pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel=connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

queue= channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

#channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue=queue.method.queue, on_message_callback=on_message_received)

print("Started consuming..")

channel.start_consuming()