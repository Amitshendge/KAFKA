from kafka import KafkaConsumer
from time import sleep

consumer = KafkaConsumer('testTopic',bootstrap_servers=['localhost:9092'])

for messsage in consumer:
    print(messsage.value)