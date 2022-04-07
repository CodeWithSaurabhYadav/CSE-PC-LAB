#/bin/python3

class student:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def print_det(self):
        print(f"{self.name} is {self.age} years old.")
        
saurabh = student("Saurabh",18)
pradeep = student("Pradeep",18)
saurabh.print_det()
pradeep.print_det()
