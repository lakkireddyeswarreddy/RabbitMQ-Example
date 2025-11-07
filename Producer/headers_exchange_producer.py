import pika

login_credentials = pika.PlainCredentials(username="guest",password="guest")

connection_properties = pika.ConnectionParameters(host="localhost",port=5672,credentials=login_credentials)

connection = pika.BlockingConnection(parameters=connection_properties)

channel = connection.channel()

channel.exchange_declare(exchange="headers_exchange", exchange_type="headers")

message = "Message routed through the exchange headers."

properties = pika.BasicProperties(headers={
    "format" : "text",
    "type" : "headers"
})

channel.basic_publish(exchange="headers_exchange",routing_key="",body=message,properties=properties)