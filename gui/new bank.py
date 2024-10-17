from tkinter import*
titlefont=("times new roman",20,"bold")
labelfont=("garamond",15,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=70,bg="sky blue")
titlelabel=Label(titleframe,text="BANK OF INDIA",bg="sky blue",fg="black",font=titlefont)
titlelabel.place(relx=0.44,rely=0.3)
titleframe.pack()
mainframe=Frame(root,width=500,height=450,bg="white")
alable=Label(mainframe,text=" ADMIN LOGIN ",bg="sky blue",font=labelfont).place(relx=0.3,rely=0.1)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.26)
mainframe.place(relx=0.35,rely=0.3)
alable=Label(mainframe,text="USER ID:",bg="pink",font=labelfont).place(relx=0.10,rely=0.25)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.26)

blable=Label(mainframe,text="PASSWORD:",bg="pink",font=labelfont).place(relx=0.06,rely=0.35)
bentry=Entry(mainframe,font=labelfont)
bentry.place(relx=0.42,rely=0.35)

clable=Label(mainframe,text=" PUBLIC LOGIN ",bg="sky blue",font=labelfont).place(relx=0.3,rely=0.5)
centry=Entry(mainframe,font=labelfont)
centry.place(relx=0.43,rely=0.26)
dlable=Label(mainframe,text="USER ID:",bg="pink",font=labelfont).place(relx=0.10,rely=0.65)
dentry=Entry(mainframe,font=labelfont)
dentry.place(relx=0.43,rely=0.65)

elable=Label(mainframe,text="PASSWORD:",bg="pink",font=labelfont).place(relx=0.06,rely=0.75)
eentry=Entry(mainframe,font=labelfont)
eentry.place(relx=0.42,rely=0.75)
root.mainloop()



