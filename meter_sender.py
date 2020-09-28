'''Copyrights 2020 Niki Papagora
email: n.papagora@gmail.com'''

try:
    import pika
    import datetime
    import time
    import random
except Exception as e:
    print("Some modules are missing.".format_map(e))

class MeterGenerator(object):
    #Prepatation of the connection to the broker and the creation of the queue
    def __init__(self, queue='power_values'):
        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue='power_values')
        self.queue = queue

    def publish(self, payload):
        self._channel.basic_publish(exchange='', routing_key='power_values', body=payload)
    
if __name__ == "__main__":
    generator = MeterGenerator(queue="power_values")
    #The sender publishes a random value between 0 and 9000 in a continuous way along with a timestamp of the message
    while True:
        message = str(random.randint(0,9000)) + " " +str(datetime.datetime.now())
        generator.publish(message)
        print("Sending values...")
        time.sleep(10)


