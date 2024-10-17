from tkinter import*
from tkinter import ttk
#global
titlefont=("time new roman",28,"bold")
labelfont=("Garamond",20,"bold")
root=Tk()
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=70,bg="blue")
titlelabel=Label(titleframe,text="YOUTUBE",bg="sky blue",fg="red",font=titlefont)
titlelabel.place(relx=0.45,rely=0.3)
titleframe.pack()
mainframe=Frame(root,width=800,height=500,bg="pink")
alabel=Label(mainframe,text="enter the main youtubers:",bg="red",fg="black",font=labelfont).place(relx=0.001,rely=0.2)
aentry=Entry(mainframe,font=labelfont)
aentry.place(relx=0.43,rely=0.2)
blabel=Label(mainframe,text="enter the support youtubers:",bg="red",fg="black",font=labelfont).place(relx=0.001,rely=0.34)
bentry=Entry(mainframe,font=labelfont)
bentry.place(relx=0.43,rely=0.35)
mainframe.place(relx=0.20,rely=0.15)
combo = ttk.Combobox(root, values=["YOUTUBERS","INSTAGRAM"],font=labelfont)
clabel=Label(mainframe,text="enter the content name:",bg="red",fg="black",font=labelfont).place(relx=0.001,rely=0.5)
combo.place(relx=0.45,rely=0.50)
combo1 = ttk.Combobox(root)
clabel=Label(mainframe,text="select the video:",bg="red",fg="black",font=labelfont).place(relx=0.001,rely=0.7)
combo1.place(relx=0.45,rely=0.65)
def videos(event):
    videos=combo.get()
    if(videos=="YOUTUBERS"):
        combo1.config(values=["vj siddhu","dayalu design","madhan gowri","track and tech","tech boss","kovai360"],font=labelfont)
    elif(videos=="INSTAGRAM"):
        combo1.config(values=["its_me_velan","smart_sanjay","karthi_livewire","call_me_mr_mukesh","msd_naveen"],font=labelfont)
        
combo.bind("<<ComboboxSelected>>",videos)
footerframe=Frame(root,width=1500,height=80,bg="sky blue")
footerlabel=Label(footerframe,text="copyright claim @",bg="sky blue",fg="red",font=titlefont)
footerlabel.place(relx=0.35,rely=0.33)
footerframe.place(relx=0.0001,rely=0.9)



sideframe=Frame(root,width=200,height=800,bg="skyblue")
rightframe=Frame(root,width=300,height=800,bg="skyblue")
rightframe.place(relx=0.83,rely=0.001)
from tkinter.ttk import *
style = Style()

style.configure('TButton', font =
			('Modern No. 20', 20, 'bold'),
					borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])


b=Button(sideframe,text="Home")
b.place(relx=0.1,rely=0.1)
b=Button(sideframe,text="About")
b.place(relx=0.1,rely=0.2)
b=Button(sideframe,text="menu")
b.place(relx=0.1,rely=0.3)
b=Button(sideframe,text="Exit", command = root.destroy)
b.place(relx=0.1,rely=0.65)
sideframe.place(relx=0.00001,rely=0.001)


n=IntVar()
c=Checkbutton(root,text="new1",variable=n).place()
n1=IntVar()
c1=Checkbutton(root,text="new2",variable=n1).place()
n2=IntVar()
c2=Checkbutton(root,text="new3",variable=n2).place()
n3=IntVar()
c=Button(root,text="click",command=lambda:select()).place()
sideframe.place(relx=0.00005,rely=0.0065)
def select():
    print(n.get())
    print(n1.get())
    print(n2.get())
    if(n.get()==1):
        print("this is male")
    else: 
        print("this is female")
root.mainloop()
root.mainloop()




