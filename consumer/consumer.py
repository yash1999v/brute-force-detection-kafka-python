import os
import json
import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Retry logic for Kafka connection
while True:
    try:
        consumer = KafkaConsumer(
            'brute-force-topic',
            bootstrap_servers=KAFKA_BROKER,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        print("Connected to Kafka Broker!")
        break
    except NoBrokersAvailable:
        print("Kafka Broker not available. Retrying in 5 seconds...")
        time.sleep(5)

for msg in consumer:
    print(f"Received Message: {msg.value}")
