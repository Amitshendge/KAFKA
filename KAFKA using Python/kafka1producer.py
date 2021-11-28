from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
for i in range(10):
    producer.send('testTopic',b'Hello Python here again')
    sleep(2)