from tkinter import*
r=Tk()
r.geometry("600x600")
l1=Label(r,text="enter the emaid id: ")
l1.grid(row=0,column=1)
l2=Label(r,text="enter the password: ")
l2.grid(row=1,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
def login():
     f=open("login.txt","x")
     f=open("login.txt","w")
     f=open("login.txt","a")
     f.write("\n")
     a=str(e1.get())
     f.write(a)
     f.write("\t")
     b=str(e2.get())
     f.write(b)
     f.write("\t")

import tkinter
from tkinter import messagebox

def hellocallback():
 tkinter.messagebox.showinfo("login page","something went wrong")
top=tkinter.Tk()

(b=Button(r,text="login",command=lambda:login())
b.grid(row=4,column=4)
B=tkinter.Button(top,text="new",command=lambda:hellocallback())
B.pack())
r.mainloop()