#/bin/python3.10

class university:
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
        university.__init__(self,name,year_of_estd,city)
    
    def display(self):
        print("Designation :",self.designation)
        print("Name :",self.name)
        print("Year of joining :",self.year_of_estd)
        print("Highest Qualification :",self.highest_qualtfication)
        print("Area of research :",self.area_of_research)
        print("Year of experience :",self.year_of_experience)
        print("Name of Institute :",self.name_of_institute)
        print("City :",self.city)
        
class lab_assistant(university):
    designation = "Lab Assistant" 
    def __init__(self, name, highest_qualification,additional_skills,year_of_joining,name_of_institute,city):
        self.highest_qualification = highest_qualification
        self.additional_skills = additional_skills
        self.year_of_joining = year_of_joining
        self.name_of_instituate = name_of_institute
        super().__init__(name,year_of_joining,city)
        
    def display(self):
        print("Designation :",self.designation)
        print("Name :",self.name)
        print("Year of joining",self.year_of_joining)
        print("Highest Qualification :",self.highest_qualification)
        print("Name of institute :",self.name_of_instituate)
        print("Additional Skills :",self.additional_skills)
        print("City :",self.city)
        
class office_assistant(university):
    designation = "Office_assistant"
    def __init__(self,name,qualification,year_of_joining,name_of_institute,city):
        self.qualification = qualification
        self.name_of_instituate = name_of_institute
        super().__init__(name,year_of_joining,city)
        
    def display(self):
        print("Designation :",self.designation)
        print("Name :",self.name)
        print("Qualtifcation :",self.qualification)
        print("Year of joining :",self.year_of_estd)
        print("Name of institute :",self.name_of_instituate)
        print(self.city)
        
class peon(university):
    designation = "Office Peon"
    def __init__(self,name,qualification,year_of_joining,name_of_institute,city):
        self.qualification = qualification
        self.year_of_joining = year_of_joining
        self.name_of_instituate = name_of_institute
        super().__init__(name,year_of_joining,city)
        
    def display(self):
        print("Designation :",self.designation)
        print("Name :",self.name)
        print("Qualtifcation :",self.qualification)
        print("Year of joining :",self.year_of_estd)
        print("Name of institute :",self.name_of_instituate)
        print("City :",self.city)
        
obj = university("Dr. Jay",2002,"Vapi")
print("*"*100)
professor1 = professor("Asst. Professor","PHD","Electronics",10,"AMTICS")
professor1.display()
print("*"*100)
lab_assistant1 = lab_assistant("Pryesh","none","Badminton","2005","AMTICS","Bardoli")
lab_assistant1.display()
print("*"*100)
office_assistant1 = office_assistant("Priya","BBA",2005,"AMTICS","Bardoli")
office_assistant1.display()
print("*"*100)
peon1 = peon("CRs","Student",2021,"AMTICS","Surat")
peon1.display()
print("*"*100)