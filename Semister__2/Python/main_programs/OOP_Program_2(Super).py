#/bin/python3.10

class Staff:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Teacher(Staff):
    def __init__(self, name, age, salary, department):
        self.salary = salary
        self.department = department
        super().__init__(name, age)
        
    def Display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("City :",self.department)
        
Teacher1 = Teacher("Rakesh",70,1000,"Student")
Teacher1.Display()