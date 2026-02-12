from connection import MySQLDB

mysql_db = MySQLDB(

)


def get_top_customers():
    cnx = self.get_connection()
    with cnx.cursor() as cursor:
        statement = """
        SELECT customer.customerNumber, 
        """


def get_customers_without_orders():
    cnx = self.get_connection()
    with cnx.cursor() as cursor:
        ...


def get_zero_credit_active_customers():
    cnx = self.get_connection()
    with cnx.cursor() as cursor:
        ...