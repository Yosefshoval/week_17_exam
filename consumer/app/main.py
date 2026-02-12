from mysql_connection import MySQLDB
from kafka_consumer import *
import os

MYSQL_HOST = os.getenv("SQL_HOST", 'mysql')
MYSQL_PORT = os.getenv("SQL_PORT", 3307)
MYSQL_USER = os.getenv("SQL_USER", 'analytics')
MYSQL_PASSWORD = os.getenv("SQL_PASSWORD", 'analytics123')
MYSQL_DATABASE = os.getenv("SQL_DATABASE", 'analytics')


MySQL_connector = MySQLDB(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
MySQL_connector.get_connection()
MySQL_connector.create_tables()

def get_records_and_save():
    while True:
        record = pull_record()
        if not record:
            continue

        inserted = MySQL_connector.insert_record(record)
        print(inserted)


get_records_and_save()