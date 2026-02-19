from tkinter import *
from tkinter.ttk import *
lp=Tk()
lp.geometry('500x300')
lp.title("Wlcome to login page")
h = Label(lp,text="Enter your name :",font=("Helavitaca",16))
h.pack()
n = Entry(lp,width=20,font=("Helavitaca",16))
n.pack()
m =Label(lp,text="",font=("helavitava",16))

def hello():
    name=n.get()
    if n.get():
        m.config(text=f'hello {n.get()}')
    else:
        m.config(text="yo forgot to enter your nmae")    
b = Button(lp,text="say Hi",command=hello)
#b.pack()
k =StringVar()
b1=Combobox(lp,textvariable=k)

b1['values']=(1,2,3,4,5)
b1.current()
b1.pack()
def select():
    s = b1.get()
    if  b1.get():
        m1.config(text=f'you selected {b1.get()}')
    else:
        m1.config(text="please select a number above")    
    
    name=n.get()
    if n.get():
        m.config(text=f'hello {n.get()}')
    else:
        m.config(text="yo forgot to enter your nmae")
butt2 = Button(lp, text="OK", command=select)
m1 = Label(lp,text="",font=("helavitaca",16))
butt2.pack()
m.pack()
m1.pack()
lp.mainloop()
