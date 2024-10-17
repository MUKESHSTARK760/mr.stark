import tkinter
root=tkinter.Tk()
root.mainloop()

from tkinter import* 
root=Tk()
root.geometry("200*200")
frame=Frame(root)
frame.pack()
root.mainloop()

from tkinter import*
root=Tk()
frame=Frame(root,bg="skyblue",width=500,height=500)
frame.pack()
root.mainloop()

import tkinter
from tkinter import messagebox

def hellocallback():
    tkinter.messagebox.showwarning("hello python","hello world")

top=tkinter.Tk()
B=tkinter.Button(top,text="new",command=lambda:hellocallback())
B.pack()
top.mainloop()
import tkinter
t=tkinter.tk()
frame=tkinter.frame(t,bg="darkblue",width=500,height=500)
b=tkinter.button(t,text="hello",activebackground="red")
b.pack()
frame.pack()
t.mainloop() 

from tkinter import*
r=Tk()
r.geometry("400x400")
l1=Label(r,text="enter the first value")
l1=grid(row=0,column=1)
l2=Label(r,text="enter the second value")
l2=grid(row=1,column=1)
l3=Label(r,text="result")
l3=grid(row=2,column=1)
e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,coloum=2)
e3=Entry(r)
e3.grid (row=2,column=2)
def add():
    a=int(e1.get)
    b=int(e2.get)
    c=a+b
    e3.delete(0.50)
    e3.insert(0,1)
b=Button(r,text="Add",command=lambda:add())
b.grid(row=3,column=3)
r.mainloop()