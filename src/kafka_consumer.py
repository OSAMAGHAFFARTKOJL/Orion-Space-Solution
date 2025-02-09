
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('orion_telemetry', bootstrap_servers='localhost:9092', auto_offset_reset='latest')

for message in consumer:
    telemetry_data = json.loads(message.value)
    print("Received:", telemetry_data)
