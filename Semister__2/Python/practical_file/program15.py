#/bin/python3.10

'''
Create a base class named university with its attributes - name, year_of_estd, and city.
Derive following class from the super class university: professor, lab_assistant,
office_assistant, and peon. Make the program choice based for user. The attributes and
method of various class are as below:
    - Attributes of professor class: designation, highest_qualification, area_of_research, year_of_joining, year_of_ experience, and name_of_institute.
    - Methods of professor class: __init__() method that gets invoked upon instantiation and takes values of class attributes. The display() method that prints class attribute values along with attributes of its super class.
    - Attributes of lab_assistant class: designation = “Lab Assistant” (static), highest_qualification, additiobnal_skilss, year_of_joining, and name_of_institue.
    - Methods of lab_assistant class: __init__() method that gets invoked upon instantiation and takes values of class attributes. The display() method that prints class attribute values along with attributes of its super class.
    - Attributes of office_assistant class: designation = “Office Assistant” (static), highest_qualification, year_of_joining, and name_of_institute.
    - Methods of office_assistant class: __init__() method that gets invoked upon instantiation and takes values of class attributes. The display() method that prints class attribute values along with attributes of its super class.
    - Attributes of peon class: job_role = “office Peon” (static), qualification, year_of_joining, and name_of_institute.
    - Methods of peon class: __init__() method that gets invoked upon instantiation and takes values of class attributes. The display() method that prints class attribute values along with attributes of its super class.
'''

#/bin/python3.10

class university:
    name = None
    year_of_estd = None
    city = None
    def __init__(self,name,year_of_estd,city):
        self.name = name
        self.year_of_estd = year_of_estd
        self.city = city
    
class professor(university):
    def __init__(self, designation,highest_qualification,area_of_research,year_of_experience,name_of_institute):
        self.designation = designation
        self.highest_qualtfication = highest_qualification
        self.area_of_research = area_of_research
        self.year_of_experience = year_of_experience
        self.name_of_institute = name_of_institute
        
    def display(self,obj):
        print("Designation :",self.designation)
        print("Name :",obj.name)
        print("Year of joining :",obj.year_of_estd)
        print("Highest Qualification :",self.highest_qualtfication)
        print("Area of research :",self.area_of_research)
        print("Year of experience :",self.year_of_experience)
        print("Name of Institute :",self.name_of_institute)
        print("City :",obj.city)

class lab_assistant(university):
    designation = "Lab Assistant"

    def __init__(self,highest_qualification, additional_skills, year_of_joining, name_of_institute):
        self.highest_qualification = highest_qualification
        self.additional_skills = additional_skills
        self.year_of_joining = year_of_joining
        self.name_of_instituate = name_of_institute

    def display(self,obj):
        print("Designation :", self.designation)
        print("Name :", obj.name)
        print("Year of extablish : ",obj.year_of_estd)
        print("Year of joining", self.year_of_joining)
        print("Highest Qualification :", self.highest_qualification)
        print("Name of institute :", self.name_of_instituate)
        print("Additional Skills :", self.additional_skills)
        print("City :", obj.city)

class office_assistant(university):
    designation = "Office_assistant"

    def __init__(self,qualification, year_of_joining, name_of_institute):
        self.qualification = qualification
        self.year_of_joining = year_of_joining
        self.name_of_instituate = name_of_institute

    def display(self,obj):
        print("Designation :", self.designation)
        print("Name :", obj.name)
        print("Qualtifcation :", self.qualification)
        print("Year of establish :", obj.year_of_estd)
        print("Year of joining :", obj.year_of_joining)
        print("Name of institute :", self.name_of_instituate)
        print(obj.city)

class peon(university):
    designation = "Office Peon"

    def __init__(self,qualification, year_of_joining, name_of_institute):
        self.qualification = qualification
        self.year_of_joining = year_of_joining
        self.name_of_instituate = name_of_institute

    def display(self,obj):
        print("Designation :", self.designation)
        print("Name :", obj.name)
        print("Qualtifcation :", self.qualification)
        print("Year of joining :", obj.year_of_estd)
        print("Name of institute :", self.name_of_instituate)
        print("City :", obj.city)



def main():
    print('''Choose the option for the value you want to enter :
    1) Professor
    2) lab Assistant
    3) Office Assistnt
    4) Peon
    5) Exit''')
    while True:
        try:
            try:
                option = int(input("Enter the option : "))
                break
            except Exception:
                print("Invalid Input")
        except KeyboardInterrupt:
            print("Invalid Input")

    if option == 1:
        while True:
            try:
                obj = university(input("Employee Name : "),int(input("Year of establish : ")),input("Employee City : "))
                obj_2 = professor(input("Enter the Designation : "),input("Enter the Highest Qualification : "),input("Enter area of research : "),int(input("Year of experience : ")),input("Name of the Institute : "))
                break
            except Exception:
                print("Please Enter the correct Details for every Field\nPease Choose the option again")
        obj_2.display(obj)

    elif option == 2:
        while True:
            try:
                obj = university(input("Employee Name : "),int(input("Year of establish : ")),input("Employee City : "))
                obj_2 = lab_assistant(input("Enter the Highest Qualification : "),input("Enter additional skills : "),int(input("Year of joining : ")),input("Name of the Institute : "))
                break
            except Exception:
                print("Please Enter the correct Details for every Field\nPease Choose the option again")
        obj_2.display(obj)
    elif option == 3:
        while True:
            try:
                obj = university(input("Employee Name : "),int(input("Year of establish : ")),input("Employee City : "))
                obj_2 = office_assistant(input("Enter the Highest Qualification : "),int(input("Year of joining : ")),input("Name of the Institute : "))
                break
            except Exception:
                print("Please Enter the correct Details for every Field\nPease Choose the option again")
        obj_2.display(obj)
    elif option == 4:
        while True:
            try:
                obj = university(input("Employee Name : "),int(input("Year of establish : ")),input("Employee City : "))
                obj_2 = office_assistant(input("Enter the Highest Qualification : "),int(input("Year of joining : ")),input("Name of the Institute : "))
                break
            except Exception:
                print("Please Enter the correct Details for every Field\nPease Choose the option again")
        obj_2.display(obj)
    elif option == 5:
        print("Thanks for using the program....")
        print("Exiting................")
        exit()
    else:
        print("Wrong Input Option")
        main()
if __name__ == "__main__":
    main()