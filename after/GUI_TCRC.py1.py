from  tkinter import*
from tkinter import ttk

root=Tk()
text=Text(root,height=2,width=30)
text.pack()

var=IntVar()
R1=Radiobutton(root,text="option 1",variable=var,value=1)
R1.pack(anchor=W)
R2=Radiobutton(root,text="option2",variable=var,value=2)
R2.pack(anchor=W)

combo=ttk.Combobox(root,values=["option 1","option 2","option 3","option 4","option 5"] )
combo.pack()

Checkbutton(root,text="new").pack()
Checkbutton(root,text="new1").pack()
root.mainloop()