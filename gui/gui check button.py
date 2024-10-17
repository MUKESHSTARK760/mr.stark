from tkinter import*
r=Tk()
n=IntVar()
c=Checkbutton(r,text="new1",variable=n).pack()
n1=IntVar()
c1=Checkbutton(r,text="new2",variable=n1).pack()
n2=IntVar()
c2=Checkbutton(r,text="new3",variable=n2).pack()
b=Button(r,text="click",command=lambda:select()).pack()
def select():
    print(n.get())
    print(n1.get())
    print(n2.get())
    if(n.get()==1):
        print("this is male")
    else: 
        print("this is female")
r.mainloop()