from confluent_kafka import Producer
import json
from os import getenv

TOPIC = getenv('KAFKA_TOPIC', '')
producer_config = {
    'bootstrap.servers' : 'kafka:9092'
}

producer = Producer(producer_config)

def callback(err, msg):
    if err:
        print(f'Error while trying to send the message: {err}')
    else:
        print(f'message: {msg.value().decode("utf-8")}')


def flush_message(message : dict):
    if message.get("orderDate"): message["orderDate"] = str(message["orderDate"])
    if message.get("shippedDate"): message["shippedDate"] = str(message["shippedDate"])
    if message.get("requiredDate"): message["requiredDate"] = str(message["requiredDate"])

    value = json.dumps(message).encode('utf-8')
    producer.produce(
        topic=TOPIC,
        value=value,
        callback=callback
    )
    producer.flush()