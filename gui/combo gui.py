from tkinter import*
from tkinter import ttk
root=Tk()
root.geometry("400x400")
l1=Label(root,text="enter the country name: ")
l1.grid(row=0,column=1)
l2=Label(root,text="enter the state name: ")
l2.grid(row=0,column=1)
l3=Label(root,text="enter the district name: ")
l3.grid(row=0,column=1)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=0,column=1)
e3=Entry(root)
e3.grid(row=3,column=4)
root.title("Combobox Example")

root.title("combo box example")
root.geometry("300x300") 
combo=ttk.Combobox(root,values=["option1","option2","option3","option4","option5",])
combo.grid(row=1,column=2)
combo1=ttk.Combobox(root)
combo1.grid()

def option_selected(event):
    option_selected=combo.get()
    print("you selected :",option_selected)
    if(option_selected=="option1"):
      combo1.config(values=["thirupur","namakkal","coimbator","erode","bangalore"])
    elif(option_selected=="option4"):
        combo1.config(values=["mayiladuthurai","sembai","covai","ooty","metupalayam"])
    elif(option_selected=="option2"):
        combo1.config(values=["karaikal","pondy","chidambaram","kodaikanal","arcot"])
    elif(option_selected=="option3"):
        combo1.config(values=["chennai","pudhukottai","thirunangur","kalahasthinathapuram","thiruvengadu"])
    elif(option_selected=="option5"):
        combo1.config(values=["mangaimadam","manikaramam","thiruvarur","needamangalam","mumbai"])
combo.bind("<<ComboboxSelected>>",option_selected)
root.mainloop()