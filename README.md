# The Mobility House -  A PV simulator application
## Keywords: Python | RabbitMQ | Ubuntu 
## Short description: 
#### An application which, among other tasks, generates simulated PV (photovoltaic) power values (in kW).
#### The components of the system are the meter_sender which generates power values and the meter_receiver which reads those values, simulates a PV value, sums them up and the writes them to a .txt file.


## Requirements 
#### We first need to install erlang:
```bash
sudo apt-get install erlang
```
#### Then we can proceed in downloading the RabbitMQ server: 
```bash
sudo apt-get install rabbitmq-server
```

#### The third step is to activate the server once it's been installed:
```bash
systemctl enable rabbitmq-server
```

## Last but not least we need to install the pika protocol 
```bash
pip install pika
```
#### For more information about RabbitMQ please refer to the official documentation https://www.rabbitmq.com/

## Run the sender and the receiver
```bash
python meter_receiver.py
python master_sender.py
```
## Additional Information
#### The order in which the scripts are being started does not matter. Even if the sender is executed first, as soon as the receiver starts it will immediately read all the values stored in the queue. 

## Contributors

#### Niki Papagora, n.papagora@gmail.com
