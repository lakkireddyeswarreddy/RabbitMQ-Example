import pika
import time

login_credentials = pika.PlainCredentials(username="guest",password="guest")

connection_properties = pika.ConnectionParameters(host="localhost",port=5672,credentials=login_credentials)

connection = pika.BlockingConnection(connection_properties)

channel = connection.channel()

channel.exchange_declare(exchange="headers_exchange",exchange_type="headers")

channel.queue_declare(queue="headers_queue")

channel.queue_bind(queue="headers_queue",exchange="headers_exchange",arguments={
    "x-match" : "all",
    "format" : "text",
    "type" : "headers"
})

def on_message_callback(channel, method, properties, body):
    print(body)

    time.sleep(1)

    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue="headers_queue", on_message_callback=on_message_callback)

channel.start_consuming()