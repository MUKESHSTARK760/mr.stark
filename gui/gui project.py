from tkinter import*
#global
titlefont=("times new roman",30,"bold")
labelfont=("britannic bold",15,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=90,bg="dark blue")
titlelabel=Label(titleframe,text="STARBUCKS",bg="white",fg="green",font=titlefont)
titlelabel.place(relx=0.40,rely=0.40)
titleframe.pack()
mainframe=Frame(root,width=800,height=400,bg="sky blue")
alable=Label(mainframe,text=" * enter the coffee name :",bg="white",font=labelfont).place(relx=0.002,rely=0.25)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.25)
blable=Label(mainframe,text=" * enter the bucks code : ",bg="white",font=labelfont).place(relx=0.002,rely=0.39)
bentry=Entry(mainframe,font=labelfont)
bentry.place(relx=0.43,rely=0.39)
clable=Label(mainframe,text=" * Enter the amount  :",bg="white",font=labelfont).place(relx=0.002,rely=0.53)
centry=Entry(mainframe,font=labelfont)
centry.place(relx=0.4,rely=0.53)
clable=Label(mainframe,text=" * Show the Balance  :",bg="white",font=labelfont).place(relx=0.002,rely=0.67)
centry=Entry(mainframe,font=labelfont)
centry.place(relx=0.4,rely=0.67)
b=Button(mainframe,text="Print reciept")
b.place(relx=0.6,rely=0.80)
mainframe.place(relx=0.25,rely=0.2)





footerframe=Frame(root,width=1500,height=90,bg="gray")
titlefont=("times new roman",30,"bold")
footerlabel=Label(footerframe,text="copy rights claim by Mr.Mukesh @",bg="red",fg="white",font=titlefont)
footerlabel.place(relx=0.35,rely=0.30)
footerframe.place(relx=0.00001,rely=0.9)

sideframe=Frame(root,width=200,height=500,bg="dark green")
from tkinter.ttk import *
style = Style()

style.configure('TButton', font =
			('Modern No. 20', 20, 'bold'),
					borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])


b=Button(sideframe,text="Menu")
b.place(relx=0.1,rely=0.1)
b=Button(sideframe,text="orders")
b.place(relx=0.1,rely=0.2)
b=Button(sideframe,text="stocks")
b.place(relx=0.1,rely=0.3)
b=Button(sideframe,text="software")
b.place(relx=0.1,rely=0.4)
b=Button(sideframe,text="custo detail")
b.place(relx=0.1,rely=0.5)
b=Button(sideframe,text="Exit", command = root.destroy)
b.place(relx=0.1,rely=0.65)
sideframe.place(relx=0.0001,rely=0.15)
root.mainloop()