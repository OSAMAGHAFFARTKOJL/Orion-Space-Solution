
from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', 
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    telemetry_data = {"temperature": random.uniform(10, 30), "pressure": random.uniform(1, 5)}
    producer.send('orion_telemetry', telemetry_data)
    time.sleep(2)
