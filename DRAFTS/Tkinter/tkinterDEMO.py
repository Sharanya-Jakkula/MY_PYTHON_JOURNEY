from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Welcome')
window.minsize(width=200,height=400)
window.maxsize(width=700,height=800)
'''v=IntVar()
def edtech():
    print(v.get())
rb1=Radiobutton(window,text='yes',value=1)
rb1.pack()
rb2=Radiobutton(window,text='no',value=0)
rb2.pack()
b1=Button(window,text='Enter',command=edtech)
b1.pack()'''
v=StringVar()
def edtech():
    if v.get()=='':
        messagebox.showwarning('Caution','It\'s empty')
    else:
        messagebox.showinfo('Successful',v.get())
    
e1=Entry(window,font=('Calibri',18),width=20,textvariable=v)
e1.pack()
b1=Button(window,text='Enter',command=edtech)
b1.pack()


window.mainloop()