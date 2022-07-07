#/bin/python3.10

class ParentClass_1:    
    name = "Saurabh"
    def __init__(self,surname):
        self.surname = surname

class ParentClass_2:
    age = 20
    
class ChildClass(ParentClass_1,ParentClass_2):
    def __init__(self):
        super().__init__("Yadav")
    def display(self):
        print(self.name,self.surname)
        print(self.age)
    
obj1 = ChildClass()
obj1.display() 