import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type=ExchangeType.fanout)

message = "Hi this is a broadcast message"

channel.basic_publish(exchange='pubsub',routing_key='', body=message)

print(f"Message sent successfully! {message}")

connection.close()



