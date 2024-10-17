class cat:
    def __init__(self,name,age):
       self.name=name 
       self.age=age
    
    def info(self):
        print(f"iam a cat.my name is{self.name}.iam{self.age}years old.")
    def make__sound(self):
        print("meow")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"iam a dog.my name is self{self.name}.iam{self.age}years old.")

    def make__sound(self):
        print("bark")

cat1=cat("kitty",2)
dog1=dog("jackson",4)
for animal in(cat1,dog1):
    animal.make__sound()
    animal.info()