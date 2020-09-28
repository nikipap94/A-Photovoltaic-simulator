'''Copyrights 2020 Niki Papagora
email: n.papagora@gmail.com'''

try:
    import pika
    import datetime
    import time
    import random
except Exception as e:
    print("Some modules are missing.".format_map(e))


#Preparation of the connection to the broker and the power_values queue
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='power_values')

def callback(ch, method, properties, body):
    #The body is of type bytes, we need to convert it into its original type so that we can process it
    received = body.decode('utf-8')
    #The first value represents the meter value sent to the broker
    meter_value = int(received.split(" ")[0])
    #The pv_power_value represents the random value created by the PV simulator. It can be between 1 and 10
    pv_power_value = random.randint(1, 10)
    final_power_value = meter_value + pv_power_value
    print("The final power value is: {}".format(final_power_value))
    #The second received value is the date
    print(received.split(" ")[1])
    #The third received value is the timestamp
    print("Received at: {}".format(received.split(" ")[2]))
    with open('final_txt', 'a') as f:
        f.write("%s,%s,%s,%s,%s\n" % (str(meter_value), str(pv_power_value), str(final_power_value), received.split(" ")[1], received.split(" ")[2]))

#The loop allows to continuously consume the values sent by the meter_sender from the queue
while True:
    channel.basic_consume(queue='power_values', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages..")
    channel.start_consuming()
