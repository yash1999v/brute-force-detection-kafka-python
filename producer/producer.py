import os
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time
import random

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Retry logic for Kafka Connection

def generate_random_ip():
    return f"192.168.1.{random.randint(1, 254)}"
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka Broker!")
        break
    except NoBrokersAvailable:
        print("Kafka Broker not available. Retrying in 5 seconds...")
        time.sleep(5)



while True:
    message = {
        "source_ip": generate_random_ip(),
        "username": "admin",
        "status": "failed_login"
    }
    print(f"Sending Message: {message}")
    producer.send('brute-force-topic', value=message)
    time.sleep(5)
