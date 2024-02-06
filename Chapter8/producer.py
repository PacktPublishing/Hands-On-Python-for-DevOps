from confluent_kafka import Producer 

import socket 

  

conf = {'bootstrap.servers': '‘<host_name>:9092', 

        'client.id': socket.gethostname()} 

  

producer = Producer(conf) 

producer.produce(topic, key="key", value="value") 
