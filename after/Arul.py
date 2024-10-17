#


from tkinter import*
r=Tk()
r.geometry("400x400")

name=Label(r,text="Enter the name")
name.grid(row=0,column=1)
Age=Label(r,text="Enter the Age")
Age.grid(row=1,column=1)
Emailid=Label(r,text="Enter the Email-id")
Emailid.grid(row=2,column=1)

e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)
