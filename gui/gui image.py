from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage 
win =Tk()
win.geometry("700x500")
img=PhotoImage(Image.open("capcap.jpg"))
label=Label(win,image=img)
label.pack()

win.mainloop()