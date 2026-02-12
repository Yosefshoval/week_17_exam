import time
import mysql.connector

class MySQLDB:
    def __init__(self, host, port, user, password, database):
        self.host = 'mysql',
        self.port = 3307,
        self.user = 'analytics',
        self.password = 'analytics123'
        self.database = 'analytics'
        self.connection = None


    def get_connection(self):
        for _ in range(5):
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    port=self.port,
                    user=self.user,
                    password=self.password
                )
                break
            except Exception as e:
                print(e)
                time.sleep(0.5)


        if not self.connection.is_connected:
            raise ConnectionError("Couldn't connect to the database")

        return self.connection

    def create_tables(self):
        cnx = self.get_connection()
        create_customer = """
           CREATE TABLE IF NOT EXISTS customer (
           id VARCHAR(255) NOT NULL PRIMARY KEY,
           type VARCHAR(255) NOT NULL,
           customerNumber VARCHAR(255) NOT NULL,
           customerName VARCHAR(255) NOT NULL,
           contactLastName VARCHAR(255) NOT NULL,
           contactFirstName VARCHAR(255) NOT NULL,
           phone INT NOT NULL,
           addressLine1 VARCHAR(255) NOT NULL,
           addressLine2 VARCHAR(255) NOT NULL,
           city VARCHAR(255) NOT NULL,
           state VARCHAR(255) NOT NULL
           postalCode INT NOT NULL,
           country VARCHAR(255) NOT NULL
           salesRepEmployeeNumber INT NOT NULL,
           creditLimit FLOAT NOT NULL
           );"""
        create_order = """
           CREATE TABLE IF NOT EXISTS order (
           id VARCHAR(255) NOT NULL PRIMARY KEY,
           type VARCHAR(255) NOT NULL,
           orderNumber INT NOT NULL,
           orderDate DATETIME NOT NULL,
           requiredDate DATETIME NOT NULL,
           shippedDate DATETIME NOT NULL,
           status VARCHAR(255) NOT NULL,
           comments VARCHAR(255),
           customerNumber INT NOT NULL
           );"""

        with cnx.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

            cursor.execute(f"USE {self.database}")

            cursor.execute(create_order)
            cursor.execute(create_customer)
            self.connection.commit()


    def insert_record(self, record: dict):
        cnx = self.get_connection()
        if not record.get('type'):
            return False
        table = record['type']
        if table == 'customer':
            sql_statement = f"""
            INSERT INTO {table} (
            id, type, customerNumber, 
            customerName, contactLastName, 
            contactFirstName, phone, addressLine1, 
            addressLine2, city, state, postalCode, 
            country, salesRepEmployeeNumber, creditLimit
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ;"""

        elif table == 'order':
            sql_statement = f"""
            INSERT INTO {table} (
            id, type, orderNumber, orderDate, 
            requiredDate, shippedDate, status, 
            comments, customerNumber
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        else:
            return False

        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(f"USE {self.database}")
            cursor.execute(sql_statement)
            cursor.execute(f'SELECT COUNT(*) FROM {table};')
            row_count = cursor.fetchone()['COUNT(*)']

        self.connection.commit()
        print(f'There are {row_count} rows in the table {table}')
        return True


