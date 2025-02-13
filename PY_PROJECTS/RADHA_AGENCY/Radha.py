from tkinter import *

#database connector
import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    database='rmaPro'
)
mycursor=db.cursor()

#tkinter code
root=Tk()
root.title("Bill management")
root.minsize(width=800,height=800)
bg=PhotoImage(file='/home/rgukt123/Downloads/watercolor.png')
backgr=Label(root,image=bg)
backgr.pack()

#variable definiton
pr1=DoubleVar()
pr2=DoubleVar()
pr3=DoubleVar()
pr4=DoubleVar()
pr5=DoubleVar()
pr6=DoubleVar()
pr7=DoubleVar()
pr8=DoubleVar()
pr9=DoubleVar()
pr10=DoubleVar()

#quan
q1=IntVar()
q2=IntVar()
q3=IntVar()
q4=IntVar()
q5=IntVar()
q6=IntVar()
q7=IntVar()
q8=IntVar()
q9=IntVar()
q10=IntVar()

#LABEL - BILL
L=Label(root,text="RADHA MILK AGENCY",font=('Calibri','25','bold'))
L.place(x=800,y=100)

L1=Label(root,text="Proprietor             :               J.RADHA",font=('Calibri','13'))
L1.place(x=830,y=160)

L2=Label(root,text="************** BILL ******************",font=('Calibri','13'))
L2.place(x=820,y=220)

bill=Button(root,text='BILL.....LOADING',background='light pink',fg='brown',font=('verdana','20'))
bill.place(x=830,y=280)

#label
l1=Label(root,text="MILK AGENCY",font=('verdana','15','bold'),fg='black',background='light pink')
l1.place(x=500,y=10)

#function
def click(sum):
    t=str(sum)
    bill.config(text=t,borderwidth=5)
    
    #quantity
    mycursor.execute("Insert INTO Quantity(GOLD,TM,SM,BCURD,SC,CUPS20,CUPS15,CUPSBOX15,BUTTERMILK,CUPSBOX20) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(q1.get(),q2.get(),q3.get(),q4.get(),q5.get(),q6.get(),q7.get(),q9.get(),q10.get(),q8.get()))
    
    #price
    mycursor.execute("Insert INTO Price(GOLD,TM,SM,BCURD,SC,CUPS20,CUPS15,CUPSBOX15,BUTTERMILK,CUPSBOX20) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(pr1.get(),pr2.get(),pr3.get(),pr4.get(),pr5.get(),pr6.get(),pr7.get(),pr9.get(),pr10.get(),pr8.get()))
    db.commit()
    
#function command
def Bfunc():
    b1.config(background='light green',fg='black',text='submitted')
    S=0
    for i in range(1,11):
        s="q{}.get()*pr{}.get()".format(i,i)
        e=eval(s)
        S+=e
    click(S)
    print(f"Total price = {S}")
    
#quantity label
qty=Label(root,text='Quantity',font=('Verdana','14'),fg='brown')
qty.place(x=220,y=50)

#price label
price=Label(root,text='Price',font=('Verdana','14'),fg='brown')
price.place(x=500,y=50)

#label-1-->gold
lab1=Label(root,text="Gold : ",font=("Calibri",15),foreground='black')
lab1.place(x=30,y=80)

#textbox-1
ent1=Entry(root,background='gray',fg='white',textvariable=q1)
ent1.place(x=220,y=85)

#entry2
p1=Entry(root,background='gray',fg='white',textvariable=pr1)
p1.place(x=500,y=85)

#label-2--tm
lab2=Label(root,text="TM    : ",font=("Calibri",15),foreground='black')
lab2.place(x=30,y=120)

#textbox=2
ent2=Entry(root,background='gray',fg='white',textvariable=q2)
ent2.place(x=220,y=125)

#p2
p2=Entry(root,background='gray',fg='white',textvariable=pr2)
p2.place(x=500,y=125)

#label-3--milk small
lab3=Label(root,text="SM   : ",font=("Calibri",15),foreground='black')
lab3.place(x=30,y=160)

#textbox=3
ent3=Entry(root,background='gray',fg='white',textvariable=q3)
ent3.place(x=220,y=165)

#p3
p3=Entry(root,background='gray',fg='white',textvariable=pr3)
p3.place(x=500,y=165)

#label-4--CURD
lab4=Label(root,text="B-CURD    : ",font=("Calibri",15),foreground='black')
lab4.place(x=30,y=200)

#textbox=4
ent4=Entry(root,background='gray',fg='white',textvariable=q4)
ent4.place(x=220,y=205)

#p4
p4=Entry(root,background='gray',fg='white',textvariable=pr4)
p4.place(x=500,y=205)

#label-5--sc
lab5=Label(root,text="SC    : ",font=("Calibri",15),foreground='black')
lab5.place(x=30,y=240)

#textboxSC
ent5=Entry(root,background='gray',fg='white',textvariable=q5)
ent5.place(x=220,y=245)

#p5
p5=Entry(root,background='gray',fg='white',textvariable=pr5)
p5.place(x=500,y=245)

#label-6 cups-20
lab6=Label(root,text="CUPS(20): ",font=("Calibri",15),foreground='black')
lab6.place(x=30,y=280)

#textbox=2  
ent6=Entry(root,background='gray',fg='white',textvariable=q6)
ent6.place(x=220,y=285)

#p6
p6=Entry(root,background='gray',fg='white',textvariable=pr6)
p6.place(x=500,y=285)

#label-7--cups 15
lab7=Label(root,text="CUPS(15) : ",font=("Calibri",15),foreground='black')
lab7.place(x=30,y=320)
#textbox=7
ent7=Entry(root,background='gray',fg='white',textvariable=q7)
ent7.place(x=220,y=325)
#p7
p7=Entry(root,background='gray',fg='white',textvariable=pr7)
p7.place(x=500,y=325)


#label-8--cups box
lab8=Label(root,text="CupsBox(20): ",font=("Calibri",15),foreground='black')
lab8.place(x=30,y=360)
#textbox-8
ent8=Entry(root,background='gray',fg='white',textvariable=q8)
ent8.place(x=220,y=365)
#p8
p8=Entry(root,background='gray',fg='white',textvariable=pr8)
p8.place(x=500,y=365)

#label-9--cups box(15)
lab9=Label(root,text="CUPS BOX(15): ",font=("Calibri",15),foreground='black')
lab9.place(x=30,y=400)
#textbox=2
ent9=Entry(root,background='gray',fg='white',textvariable=q9)
ent9.place(x=220,y=405)
#p9
p9=Entry(root,background='gray',fg='white',textvariable=pr9)
p9.place(x=500,y=405)

#label-10-buttermilk
lab10=Label(root,text="Butter milk : ",font=("Calibri",15),foreground='black')
lab10.place(x=30,y=440)
#textbox-9
ent10=Entry(root,background='gray',fg='white',textvariable=q10)
ent10.place(x=220,y=445)
#p10
p10=Entry(root,background='gray',fg='white',textvariable=pr10)
p10.place(x=500,y=445)
#button
b1=Button(root,background='light pink',borderwidth=8,fg='black',text='SUBMIT',command=Bfunc,width=30)
b1.place(x=350,y=500)

#run
root.mainloop()
