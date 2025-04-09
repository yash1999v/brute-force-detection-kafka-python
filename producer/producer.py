import os
import sys
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time
import random
from datetime import datetime  # Added for timestamp

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Fixed IP List
ip_list = [
    "10.0.0.1",  # Attacker
    "10.0.0.2",  # Attacker
    "192.168.1.10",
    "192.168.1.12",
    "192.168.1.13",
    "192.168.1.14",
    "192.168.1.15",
    "192.168.1.16",
    "192.168.1.17",
    "192.168.1.18",
    "192.168.1.19",

]

# Retry logic for Kafka Connection
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Connected to Kafka Broker!")
        sys.stdout.flush()
        break
    except NoBrokersAvailable:
        print("Kafka Broker not available. Retrying in 5 seconds...")
        sys.stdout.flush()
        time.sleep(5)

# Generate Logs
while True:
    ip = random.choice(ip_list)

    if ip in ["10.0.0.1", "10.0.0.2"]:
        status = "failed_login" if random.random() < 0.8 else "success_login"
    else:
        status = "success_login" if random.random() < 0.9 else "failed_login"

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp

    message = {
        "source_ip": ip,
        "username": "admin",
        "status": status,
        "timestamp": current_time  # Added timestamp to message
    }

    print(f"[{current_time}] Sending Message: {message}")
    sys.stdout.flush()
    producer.send('brute-force-topic_3', value=message)
    time.sleep(5)
