import time
import json
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

KAFKA_TOPIC = 'brute-force-topic'

# Keep trying until Kafka is ready
while True:
    try:
        consumer = KafkaConsumer(
            KAFKA_TOPIC,
            bootstrap_servers=['kafka:9092'],
            auto_offset_reset='earliest',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        print("Kafka Connected Successfully! Consumer is running... Waiting for messages...")
        break
    except NoBrokersAvailable:
        print("Kafka not ready, retrying in 5 seconds...")
        time.sleep(5)

for message in consumer:
    print(f"Received message: {message.value}")
