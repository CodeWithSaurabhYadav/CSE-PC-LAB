#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Create a class named employee having attributes - emp_name, emp_age, and emp_city.
Create a method named get_data() in employee class that takes user input for these
attributes. Derive a class named emp_derived() from the employee class, having an
__init__() method that displays the attributes of the employee class upon instantiation.
'''

class Employee:
    emp_name = None
    emp_age = None
    emp_city = None
    def get_data(self,emp_name,emp_age,emp_city):
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_city = emp_city

class emp_derived(Employee):
    def __init__(self,obj):
        print("The employee name is :",obj.emp_name)
        print("The employee age is  :",obj.emp_age)
        print("The employee lives in  :",obj.emp_city)

obj = Employee()
obj.get_data("Saurabh",18,"Vapi")
emp_obj = emp_derived(obj)