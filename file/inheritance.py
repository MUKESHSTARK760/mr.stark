class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)

class college(person):
    def __init__(self,fname,lname,college):
     super().__init__(fname,lname)        
     self.college=college
    def print(self):
        print(self.firstname,self.lastname,self.college)

class student(college):
    def __init__(self,fname,lname,class1,degree):
     super(). __init__(fname,lname,class1)
     self.Degree=degree
mani=student("mani","kannan","abc","m.e")
mani.printname()
mani.print()
print(mani.Degree)   

