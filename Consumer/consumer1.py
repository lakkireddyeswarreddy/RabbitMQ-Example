import time
import pika

login_credentials = pika.PlainCredentials(username="guest",password="guest")

connection_parameters = pika.ConnectionParameters(host="localhost",port=5672,credentials=login_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange="direct_exchange",exchange_type="direct")

channel.queue_declare(queue="first_queue")

channel.queue_bind(exchange="direct_exchange",queue="first_queue",routing_key="queue")

def on_message_callback(channel, method, properties, body):

    print(body)
    time.sleep(1)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="first_queue", on_message_callback=on_message_callback,auto_ack=False)

channel.start_consuming()