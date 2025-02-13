#to connect python with the mysql and work upon it
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='DBMS'
)

mycursor=db.cursor()
#mycursor.execute("CREATE TABLE Person (name varchar(50),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("INSERT INTO Person(name,age) VALUES(%s,%s)",('Tim',19))
mycursor.execute("INSERT INTO Person(name,age) VALUES(%s,%s)",('Joe',17))
#db.commit()
'''for x in mycursor:
    print(x)'''
mycursor.execute("SELECT * FROM Person")
for i in mycursor:
    print(i)