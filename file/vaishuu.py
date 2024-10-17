class newclass:
     n=9
     def __init__(self,name):
        self.name=name
        print("new1")
     def print1(self):
         print(self.name)

obj=newclass("vaishu weds mukesh, velan weds nisha, sanjay weds vishal")
print(obj.n)
obj.print1()
obj1=newclass("young")
print(obj1.n)
obj1.n=45
print(obj.n,obj1.n)