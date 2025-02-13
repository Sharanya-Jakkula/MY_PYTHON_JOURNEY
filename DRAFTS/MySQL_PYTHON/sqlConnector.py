import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector import MySQLConnection
import getpass4

try:
    password=getpass4.getpass("Enter password : ")
    cnx = MySQLConnection.connector.connect(user='root', password=password,host='127.0.0.1',database='DBMS')
    # Your code for database operations goes here

except Error as e:
    print(f"Error: {e}")

finally:
    if cnx.is_connected():
        cnx.close()
        print("Connection closed.")


