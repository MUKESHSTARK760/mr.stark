from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage
root=Tk()
#global
titlefont=("times new roman",20,"bold")
labelfont=("garamond",15,"bold")
root.geometry("1500x700")
titleframe=Frame(root,width=1500,height=70,bg="purple")
titlelabel=Label(root,text="student",bg="purple",fg="white",font=titlefont)
titlelabel.place(relx=0.35,rely=0.1)
titleframe.pack()
root.geometry("1500x700")
img=PhotoImage(Image.open("beach.jpg"))
label=Label(root,image=img)
label.place(relx=0.000001,rely=0.1)
bitleframe=Frame(root,width=1500,height=70,bg="purple")
bitlelabel=Label(root,text="student",bg="sky blue",fg="green",font=titlefont)
bitlelabel.place(relx=0.5,rely=0.35)
bitleframe.pack()

root.mainloop()
