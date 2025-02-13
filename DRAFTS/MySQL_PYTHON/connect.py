import mysql.connector 
from mysql.connector import MySQLConnection
import getpass4
password=getpass4.getpass("Enter the password :")
try:
    connect=MySQLConnection.connector.connect(user='root',host='127.0.0.1',password=password,database='DBMS')
    print("Successfully created...")
    print(connect)
except Exception:
    print("ERROR OCCURRED")