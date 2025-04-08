import time
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import random
import datetime

KAFKA_TOPIC = 'brute-force-topic'

# Wait until Kafka is ready
while True:
    try:
        producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        print("Kafka Connected Successfully!")
        break
    except NoBrokersAvailable:
        print("Kafka not ready, waiting for 5 seconds...")
        time.sleep(5)

# Dummy data generator
while True:
    log_data = {
        "ip": f"192.168.1.{random.randint(1, 255)}",
        "status": random.choice(["FAILED", "SUCCESS"]),
        "timestamp": str(datetime.datetime.now())
    }

    print(f"Sending Data: {log_data}")

    producer.send(KAFKA_TOPIC, log_data)
    producer.flush()

    time.sleep(3)  # Send data every 3 seconds
