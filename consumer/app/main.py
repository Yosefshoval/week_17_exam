from mysql_connection import MySQLDB

MySQL_connector = MySQLDB(
    host=SQL_HOST,
    port=SQL_PORT,
    user=SQL_USER,
    password=SQL_PASSWORD,
    database=SQL_DATABASE
)
