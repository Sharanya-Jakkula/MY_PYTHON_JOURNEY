import mysql.connector

cnx = mysql.connector.connect(user='root', password='Password@123',
                              host='127.0.0.1',
                              database='DBMS')
cnx.close()
