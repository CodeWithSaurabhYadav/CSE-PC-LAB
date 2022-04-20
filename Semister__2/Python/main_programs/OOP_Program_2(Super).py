#/bin/python3.10

# This is the staff class that contains initial
# Parent class
class Staff:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# This is the Teacher class 
# Child class which is derived from Staff() Class
class Teacher(Staff):
    def __init__(self, salary, department):
        self.salary = salary
        self.department = department
        super().__init__("Saurabh", 18)
        
    def Display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("City :",self.department)
        
Teacher1 = Teacher(1000,"Student")
Teacher1.Display()