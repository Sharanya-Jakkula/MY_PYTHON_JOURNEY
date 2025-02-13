#To create the login portal and store the data
from tkinter import *
import os
#database
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='login'
)

#main project
os.chdir('/home/rgukt123/MY_PY_JOURNEY/PY_PROJECTS/LOGINTkinter')
root=Tk()
root.title('Login')
root.minsize(width=500,height=500)
root.maxsize(width=900,height=900)
#first column
l1=Label(root,text='Username : ')
l1.place(x=30,y=30)
#--->variable
v=StringVar()
k=StringVar()
#func
def func():
    b1.config(text='submitted',fg='black',bg='orange')
    #print(v.get()+"\n"+k.get())
    #sql connect
    mycursor=db.cursor()
    #mycursor.execute("CREATE TABLE Person (name varchar(50),age smallint UNSIGNED,personID int PRIMARY KEY AUTO_INCREMENT)")
    #mycursor.execute("INSERT INTO Person(name,age) VALUES(%s,%s)",('Tim',19))
    mycursor.execute("INSERT INTO LOGIN(USERNAME,PWD) VALUES(%s,%s)",(v.get(),k.get()))
    db.commit()
    '''for x in mycursor:
    print(x)'''
    mycursor.execute("SELECT * FROM LOGIN")
    for i in mycursor:
        print(i)

    #file writing
    with open('login.txt','a') as f:
        v1=v.get()
        k1=k.get()
        f.write(v1+'\t'+k1+'\n')
        
#entry
e1=Entry(root,width=30,textvariable=v)
e1.place(x=120,y=30)
#second column
l2=Label(root,text='Password : ')
l2.place(x=30,y=60)
#entry
e2=Entry(root,width=30,textvariable=k)
e2.place(x=120,y=60)
#submit
b1=Button(root,text='SUBMIT',fg='black',bg='yellow',command=func)
b1.place(x=170,y=100)
root.mainloop()