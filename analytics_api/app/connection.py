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
