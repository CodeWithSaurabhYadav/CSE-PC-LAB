#/bin/python3.10

from unicodedata import name


class ParentClass:
    name = "Saurabh"
    
class ChileClass_1(ParentClass):
    surname = "Yadav"
    
class ChildClass_2(ChileClass_1):
    def display(self):
        print(self.name)
        print(self.surname)
        
obj = ChildClass_2()
obj.display()