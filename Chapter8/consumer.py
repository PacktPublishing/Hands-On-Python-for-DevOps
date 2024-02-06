from confluent_kafka import Consumer 

  

conf = {'bootstrap.servers': ‘<host_name>:9092', 

        'group.id': ‘<group_id_here>’, 

        'auto.offset.reset': 'smallest'} 

  

consumer = Consumer(conf) 

while True: 

	msg = consumer.poll(timeout=1.0) 

	if msg is None: continue 

	break 
