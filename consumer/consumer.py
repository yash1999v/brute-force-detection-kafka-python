import os
import json
import time
import logging
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from collections import defaultdict, deque
from datetime import datetime, timedelta

KAFKA_BROKER = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "alerts.log")

# Logging Setup (Console + File)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

# Threshold Config
FAILED_ATTEMPTS_THRESHOLD = 3  # Attempts
TIME_WINDOW = 60  # Seconds

failed_attempts = defaultdict(lambda: deque(maxlen=FAILED_ATTEMPTS_THRESHOLD))

# Function to generate clean timestamp for log message
def log_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Kafka Connection Retry Logic
while True:
    try:
        consumer = KafkaConsumer(
            'brute-force-topic_3',
            bootstrap_servers=KAFKA_BROKER,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        logging.info(f"{log_timestamp()} Connected to Kafka Broker!")
        break
    except NoBrokersAvailable:
        logging.warning(f"{log_timestamp()} Kafka Broker not available. Retrying in 5 seconds...")
        time.sleep(5)

# Main Consumer Logic
for msg in consumer:
    event = msg.value
    source_ip = event.get("source_ip")
    status = event.get("status")

    logging.info(f"{log_timestamp()} Received login attempt from {source_ip} - Status: {status}")

    if status == "failed_login":
        current_time = datetime.now()
        failed_attempts[source_ip].append(current_time)

        if len(failed_attempts[source_ip]) == FAILED_ATTEMPTS_THRESHOLD:
            time_diff = (current_time - failed_attempts[source_ip][0]).total_seconds()

            if time_diff <= TIME_WINDOW:
                logging.error(f"{log_timestamp()} BRUTE FORCE DETECTED from {source_ip}")
            else:
                logging.warning(f"{log_timestamp()} Suspicious activity from {source_ip}")
