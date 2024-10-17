from tkinter import*
def sel():
    selection="you selected the option"+str(var.get())
    
    Label.config(text=selection)
root=Tk()
var=IntVar()
r1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
r1.pack() 
r2=Radiobutton(root,text="option1",variable=var,value=2,command=sel)
r2.pack()       
r3=Radiobutton(root,text="option1",variable=var,value=3,command=sel)
r3.pack()
Label=Label(root)
Label.pack()
root.mainloop()    