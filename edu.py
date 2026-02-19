from tkinter import *
from tkinter.ttk import *
root=Tk()
root.title("Education")
root.geometry('300x400')
heading = Label(root, text="EDUCATION",border=3,anchor='center')
heading.pack()
entr_name =Label(root,text="*Please enter your name below*",font=("calibri",12))
entr_name.pack()
name = Entry(root,width=20,font=("helavitaca",14))
name.pack()
name_warn = Label(root,text="",foreground="pink")
name_warn.pack()
def sayhi():
    if name.get():
        name_warn.config(text=f'Hii {name.get()}',foreground="Black")
        entr_strm.pack()
        main_strm.pack()
        srtm_warn.pack()
        b2.pack()
    else:
        name_warn.config(text="Please Enter your name First!!",foreground="red")  
sub_name =Button(root,text="submit Name",command=sayhi)          
sub_name.pack()
k1 =StringVar()
main_strm =Combobox(root,textvariable=k1)
main_strm['values']=("Arts","Commeres","Science")
main_strm.current(0)
entr_strm = Label(root,text="Enter Your stream",font=("calibri",12),padding=10)
m3 =Label(root,text="")
srtm_warn =Label(root , text="")
entr_quli = Label(root,text=("enter qualificatin level"),font=("calibri",12),padding=10)
global stream
def distream():
  stream = main_strm.get()
  if stream :
    entr_quli.pack(after=b2)
    c2.pack(after=entr_quli)
    quli_warn.pack()    
    b3.pack()
    
    match stream:
     case "Arts":
        c2.config(values=("B.A.","M.A."))
     case "Commeres":
        c2.config(values=("B.Com","M.Com"))
     case "Science":
        c2.config(values=("B.Sc","M.Sc","B.Tech","M.Tech"))
     case _:
        pass 
  else:
     srtm_warn.config(text="Please seelct an option",font=("Helavitaca",12),foreground="red")          
b2 = Button(root,text="submit stream",command=distream)
m3.pack()
k2=StringVar()
c2 =Combobox(root,textvariable=k2)
c2['values']=()
global qu
def prtall():
   qu=c2.get()
   if qu:
   
    root2 =Tk()
    root2.geometry('800x300')
    m5 = Label(root2 , text="")
    thk = Label(root2,text=f'Thank you {name.get()} !',font=("times new roman",25),foreground="green",padding=20)
    m5.config(text=f'Hi {name.get()}, \n Your student of {main_strm.get()} and doing/completed {qu} qualification',font=("calibri",20))
    m5.pack(anchor='w')
    thk.pack(anchor='w')
    root2.mainloop()
   else:
      quli_warn.config(text="please enter Qualification",font=("helavitaca",14),foreground="red")        

b3 = Button(root,text="Submit all",command=prtall)
quli_warn=Label(root,text="")
root.mainloop()