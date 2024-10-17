# class student:
#     a="class 1"
#     b=5
#     def new1(self):
#         print("call able")
#         print(self)


# obj=student()
# print(obj.b)
# obj.new1()
# print(obj)

# obj1=student()
# obj1.b=7
# print(obj1.b)
# obj1.new1()
# print(obj1)
# class c1:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("this is function")
#     def func1(self):
#         print(self.name,self.age)

# c=c1("ramesh",45)
# c.func1() 
# print(c.name)   


""" class c2:
    name="some name"
    def func1(self):
        print(self)
obj=c2()
print(obj.name)
print(obj)
obj.func1()   """
 
class employe:
    def __init__(self,name,age,salary,):
        self.name=name
        self.age=age
        self.salary=salary
        print("salary is increase in monthly")
    def read(self):
        print(self.name,self.age,self.salary)
    def __str__(self):
        return str(self.name)
obj=employe("rajam",22,100000)
obj.read()
print(obj) 




 