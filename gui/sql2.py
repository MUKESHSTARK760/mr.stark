'''import pymysql as mysql    
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
 print(x)
#createtable
import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="moni")
cursor=connection.cursor()
#cursor.execute("CREATE TABLE department(department_id int PRIMARY KEY,department_name varchar(50))")
cursor.execute("show tables")
print("number of tables in data base:")
for x in cursor:
 print("\t",x)
 import pymysql as mysql

cursor=connection.cursor()
cursor.execute("CREATE TABLE employee3(employee3_id int PRIMARY KEY,employee_name varchar(50))")
cursor.execute("show tables")
print("number of tables in data base:")
for x in cursor:
 print("\t",x)'''

from tkinter import*
#global
titlefont=("times new roman",20,"bold")
labelfont=("garamond",15,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=70,bg="purple")
titlelabel=Label(titleframe,text="STAFF MANAGEMENT REGISTER",bg="sky blue",fg="green",font=titlefont)
titlelabel.place(relx=0.34,rely=0.35)
titleframe.pack()
mainframe=Frame(root,width=500,height=550,bg="pink")
alable=Label(mainframe,text=" (i) Enter the Name :",bg="pink",font=labelfont).place(relx=0.002,rely=0.25)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.26)
blable=Label(mainframe,text=" (ii) Enter the roll no : ",bg="pink",font=labelfont).place(relx=0.002,rely=0.39)
bentry=Entry(mainframe,font=labelfont)
bentry.place(relx=0.43,rely=0.4)
clable=Label(mainframe,text=" (iii) Applicant Age:",bg="pink",font=labelfont).place(relx=0.002,rely=0.53)
centry=Entry(mainframe,font=labelfont)
centry.place(relx=0.4,rely=0.53)
clable=Label(mainframe,text=" (iv) Enter the DOB :",bg="pink",font=labelfont).place(relx=0.002,rely=0.67)
centry=Entry(mainframe,font=labelfont)
centry.place(relx=0.4,rely=0.67)
a=Button(mainframe,text="ADD")
a.place(relx=0.08,rely=0.80)
b=Button(mainframe,text="DELETE")
b.place(relx=0.23,rely=0.80)
c=Button(mainframe,text="UPDATE")
c.place(relx=0.40,rely=0.80)
d=Button(mainframe,text="REFRESH")
d.place(relx=0.57,rely=0.80)
mainframe.place(relx=0.002,rely=0.11)  

 

footerframe=Frame(root,width=1500,height=90,bg="gray")
titlefont=("times new roman",30,"bold")
footerlabel=Label(footerframe,text="website created by A1 Ideas@",bg="red",fg="white",font=titlefont)
footerlabel.place(relx=0.35,rely=0.30)
footerframe.place(relx=0.00001,rely=0.9)

sideframe=Frame(root,width=2000,height=1000,bg="yellow")
from tkinter.ttk import *
style = Style()

style.configure('TButton', font =
			('Modern No. 20', 20, 'bold'),
					borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])

root.mainloop()

def ADD(self):
        NAME=self.aentry.get()
        REGISTERNUMBER=self.bentry.get()
        STUDENTAGE=self.centry.get()
        STUDENTDOB=self.dentry.get()
        self.tree.insert("",index=0,values=(NAME,REGISTERNUMBER,STUDENTAGE,STUDENTDOB))
       
def DELETE(self):
       item=self.tree.selection()
       self.tree.delete(item)
def UPDATE(self):
        NAME=self.aentry.get()
        REGISTERNUMBER=self.bentry.get()
        STUDENTAGE=self.centry.get()
        STUDENTDOB=self.dentry.get()
        item=self.tree.selection()
        self.tree.item(item,values=(NAME,REGISTERNUMBER,STUDENTAGE,STUDENTDOB))
def REFRESH(self):
        NAME=self.aentry.delete(0,END)
        REGISTERNUMBER=self.bentry.delete(0,END)
        STUDENTAGE=self.centry.delete(0,END)
        STUDENTDOB=self.dentry.delete(0,END)
        item=self.tree.delete()
        self.tree.item(item,values=(NAME,REGISTERNUMBER,STUDENTAGE,STUDENTDOB))
          
      #self.Frame_1=Frame(self.root ,heigth=550, width=200, bd=2, relief=GROOVE,bg="yellow")
      #self.Frame_1.pack()
root=Tk()
root.title("student data base")
root.resizable(False,False)
root.geometry("1200x600")
student(root)
root.mainloop()
    