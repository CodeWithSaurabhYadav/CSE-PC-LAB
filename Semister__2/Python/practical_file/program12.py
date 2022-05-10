#/bin/python3.10

'''
Create a class named student having attributes - std_name, std_age, std_branch, and
std_city. Create a method named get_data() in student class that takes user input for these
attributes and a method named display() that prints the attribute values on the terminal.
Call both the methods by creating an instance std_obj of the class student
'''

class student:
    def get_data(self,name,age,branch,city):
        self.std_name = name
        self.std_age = age
        self.std_branch = branch
        self.std_city = city
    
    def display(self):
        print("Student name :",self.std_name)
        print("Stutent age :",self.std_age)
        print("Student branch :",self.std_branch)
        print("Student city :",self.std_city)
        
std_obj = student()
std_obj.get_data("saurabh",18,"B.Tech CSE","Vapi")
std_obj.display()
