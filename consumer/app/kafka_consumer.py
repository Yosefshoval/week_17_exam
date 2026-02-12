from confluent_kafka import Consumer
from os import getenv

KAFKA_TOPIC = getenv('KAFKA_TOPIC')

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe([KAFKA_TOPIC])

print(f"Consumer is running and subscribed to {KAFKA_TOPIC} topic")


def pull_record():
    try:
        msg = consumer.poll(1.0)
        if msg is None:
            return None
        if msg.error():
            print("Error:", msg.error())
            return False
        value = msg.value().decode("utf-8")
        record = json.load(value)
        print(f"Received order: {record['type']}")
        return record

    except Exception as e:
        print(e)
        return False