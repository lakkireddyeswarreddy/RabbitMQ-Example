import pika

login_credentials = pika.PlainCredentials(username="guest",password="guest")

connection_parameters = pika.ConnectionParameters(host="localhost",port=5672,credentials=login_credentials)

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

#sends the messages to the queue that matches the exact routing key
channel.exchange_declare(exchange="direct_exchange",exchange_type="direct")

#sends the messages to the queue based on the part of routing key and the routing key look like "user.*", "user.#", where * is one word and # is zero or more words.
channel.exchange_declare(exchange="topic_exchange",exchange_type="topic")

#sends to all the queues that are binded to the exchange irrespective of the routing key
channel.exchange_declare(exchange="fanout_exchange",exchange_type="fanout")

#sends messages based on the headers (Advanced)
channel.exchange_declare(exchange="headers_exchange",exchange_type="headers")


channel.queue_declare(queue="first_queue")

channel.queue_bind(exchange="direct_exchange",queue="first_queue",routing_key="queue")

message = "My first message through RabbitMQ message broker."

channel.basic_publish(exchange="direct_exchange",routing_key="queue",body=message)

