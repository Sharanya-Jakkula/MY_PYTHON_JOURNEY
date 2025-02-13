#To create the login portal and store the data
from tkinter import *
import os
os.chdir('/home/rgukt123/MY_PY_JOURNEY/PY_PROJECTS/LOGINTkinter')
root=Tk()
root.title('Login')
root.geometry('500x500')
#root.minsize(width=500,height=500)
#root.maxsize(width=800,height=800)
bg=PhotoImage(file='/home/rgukt123/Downloads/photo/moon.png')
l=Label(root,image=bg)
l.pack()
#first column
l1=Label(root,text='Username : ',borderwidth=2)
l1.place(x=30,y=30)
#--->variable
v=StringVar()
k=StringVar()
#func
def func():
    b1.config(text='submitted',fg='black',bg='orange')
    print(v.get()+"\n"+k.get())
    with open('login.txt','a') as f:
        v1=v.get()
        k1=k.get()
        f.write(v1+'\t'+k1+'\n')
#entry
e1=Entry(root,width=30,textvariable=v,border=5)
e1.place(x=120,y=30)
#second column
l2=Label(root,text='Password : ')
l2.place(x=30,y=60)
#entry
e2=Entry(root,width=30,textvariable=k,border=5)
e2.place(x=120,y=60)
#submit
b1=Button(root,text='SUBMIT',fg='black',bg='yellow',command=func)
b1.place(x=170,y=100)
root.mainloop()