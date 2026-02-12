from kafka_publisher import *
from mongo_connection import MongoDB
import time

client = MongoDB()
if client:
    print('mongodb client is connected')
else:
    print('client is not connected')

n = 40

def get_records():
    is_first = True
    while True:
        for _ in range(n):
            try:
                if is_first:
                    records = client.get_n_records(n=n)
                else:
                    records = client.get_n_records(n=n, skip=n)
                if not records:
                    print('All records are sent to Kafka.')
                    break
            except Exception as e:
                print(e)
                continue

            for record in records:
                try:
                    flush_message(message=record)
                    time.sleep(0.5)
                except Exception as e:
                    print(e)
    return True


get_records()