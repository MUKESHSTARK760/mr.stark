#f=open("text.txt","x")
f=open("queen.txt","w")
a=input("enter the employee name :")
b=input("enter the employee no ;")
f=open("text.txt","a")
f.write("\t next")
f=open("text.txt","r")
a=f.read()
print()