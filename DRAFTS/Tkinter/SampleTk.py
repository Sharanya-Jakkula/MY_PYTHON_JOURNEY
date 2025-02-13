from tkinter import *
import os
window=Tk()
window.title('Demonstration')
#adjust size
window.minsize(width=100,height=200)
window.maxsize(width=300,height=800)
#add label
#l1=Label(window,text='Great Learning',bg='blue',fg='white',width=40)
#l1.pack()
#l1.grid(row=0,column=1)
#l1.place(x=50,y=100)
'''i1=PhotoImage(file='home/rgukt123/Downloads/tiger-8214815_1280.png')
l1=Label(window,image=i1)'''

#-button
'''b1=Button(window,text='Enter',bg='blue',fg='yellow')
b1.pack()'''

#entry
'''e1=Entry(window,width=20,bd=5,font=('Calibri',20))#bd=border
e1.pack()'''
#check button
'''cb=Checkbutton(window,text='Male')
cb.pack()'''
#frame
'''f1=Frame()
f1.pack()
f2=Frame()
f2.pack(side=BOTTOM)
l1=Label(f1,text='Great learning')
l1.pack()
l2=Label(f2,text='bottom')
l2.pack()
'''
#listbox
lb=Listbox(window,width=20)
lb.pack()
l1=['DHONI','VIRAT','SHREYAS','SKY','SIRAJ']
for i in l1:
    lb.insert(END,i)
def edtech():
    lb.delete(ANCHOR)#ANCHOR to remove one by one
b1=Button(window,text='remove',bg='yellow',fg='white',command=edtech)
b1.pack()
window.mainloop()