from tkinter import*
#global
titlefont=("times new roman",20,"bold")
labelfont=("garamond",15,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=70,bg="purple")
titlelabel=Label(titleframe,text="student",bg="sky blue",fg="green",font=titlefont)
titlelabel.place(relx=0.5,rely=0.35)
titleframe.pack()
mainframe=Frame(root,width=500,height=450,bg="pink")
alable=Label(mainframe,text=" (i) enter the student roll no:",bg="pink",font=labelfont).place(relx=0.002,rely=0.25)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.26)
blable=Label(mainframe,text=" (ii) enter the student personal code : ",bg="pink",font=labelfont).place(relx=0.002,rely=0.39)
bentry=Entry(mainframe,font=labelfont)
bentry.place(relx=0.43,rely=0.4)
b=Button(mainframe,text="Add members")
b.place(relx=0.6,rely=0.80)
mainframe.place(relx=0.35,rely=0.3)





footerframe=Frame(root,width=1500,height=90,bg="gray")
titlefont=("times new roman",30,"bold")
footerlabel=Label(footerframe,text="website created by A1 Ideas@",bg="red",fg="white",font=titlefont)
footerlabel.place(relx=0.35,rely=0.30)
footerframe.place(relx=0.00001,rely=0.9)

sideframe=Frame(root,width=200,height=800,bg="yellow")
from tkinter.ttk import *
style = Style()

style.configure('TButton', font =
			('Modern No. 20', 20, 'bold'),
					borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])


b=Button(sideframe,text="Menu")
b.place(relx=0.1,rely=0.1)
b=Button(sideframe,text="character")
b.place(relx=0.1,rely=0.2)
b=Button(sideframe,text="Exit", command = root.destroy)
b.place(relx=0.1,rely=0.65)
sideframe.place(relx=0.0001,rely=0.1)
root.mainloop()