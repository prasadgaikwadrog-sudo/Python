from tkinter import *
root = Tk()
root.title("Python GUI")

global f 
f=1
def doyt():
    global f
    if f==1:
       first_label.config(text="BYE BYE!")
       f=0
    else:
        first_label.config(text="First GUI")
        f=1

name = Entry(root,width=20,font=("calibri",20))
name.pack()     



first_label = Label(root ,text="First GUI")

first_label.pack(padx=10)

one_canvas = Canvas(root,bg="orange",highlightbackground="red",highlightcolor="purple",bd=5,relief="groove")
abutton=Button(root, text="click here" , command =doyt ,bg="blue",fg="yellow")
sec_label=Label(root,text="second label")

#one_canvas.pack()
abutton.pack()
sec_label.pack()


root.mainloop()