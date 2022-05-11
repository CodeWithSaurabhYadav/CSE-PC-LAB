class uka_University:
    def _init_(self,name,year,city):
        self.name=name
        self.year = year
        self.city=city
class proffesor(uka_University):
    designation ="Proffesor"
    def _init_(self,name_of_instiute):
        self.name_of_instiute=name_of_instiute
        super()._init_(name,year,city)

    def display(self):
        print('*'*100,'\n')
        print(self.designation)
        print('Name: ' ,self.name)
        print('Year of establish of university: ',self.year)
        print('Institue name : ',self.name_of_instiute)
        print('Place :',self.city)

        

class lab_assistant(uka_University):
      designation ="Lab_Assistant"
      def _init_(self,high_qualification,additional_skills,year_of_joining,name_of_instiute):
          self.high_qualification=high_qualification
          self.additional_skills=additional_skills
          self.year_of_joining=year_of_joining
          self.name_of_institue=name_of_instiute
          super()._init_(name,year,city)
           
      def display(self):
        print('*'*100,'\n') 
        print(self.designation)
        print('Name: ' ,self.name)
        print('Additional_skills: ',self.additional_skills)
        print('Year of joining: ',self.year_of_joining)
        print('Year of establish of university: ',self.year)
        print('Institue name: ',self.name_of_institue)
        print('Place :',self.city)


class office_assistant(uka_University):
    designation="Office Assistant"
    def _init_(self,high_qualification,year_of_joining,name_of_instiute):
          self.high_qualification=high_qualification
          self.year_of_joining=year_of_joining
          self.name_of_institue=name_of_instiute
          super()._init_(name,year,city)
           
    def display(self):
        print('*'*100,'\n')
        print(self.designation)
        print('Name: ' ,self.name)
        print('Year of establish of university: ',self.year)
        print('Qulification: ',self.high_qualification)
        print('Year of joining: ',self.year_of_joining)
        print('Institue name: ',self.name_of_institue)
        print('Place :',self.city)

class peon(uka_University):
    designation ="Peon"

    def _init_(self,qualification,year_of_joinimg,name_of_institue):
          self.qualification=qualification
          self.year_of_joining=year_of_joinimg
          self.name_of_institue=name_of_institue
          super()._init_(name,year,city)
          

    def display(self):
        print('*'*100,'\n')
        print(self.designation)
        print('Name: ' ,self.name)
        print('Year of establish of university: ',self.year)
        print('Qulification: ',self.qualification)
        print('Year of joining: ',self.year_of_joining)
        print('Institue name: ',self.name_of_institue)
        print('Place :',self.city)

# uka university
name=input("Enter the name = ")        
year=int(input("Enter the year where they established = "))        
city=input("Enter the city = ")        
uk=uka_University(name,year,city)
print('*'*100,'\n')

choice=input('''
1 for professor
2 for lab assistant
3 for office assistant
4 for peon
choice any one : ''')
   
# professor
if choice =='1':
    print('*'*100,'\n')
    name_institue=input("Enter the name of institue = ")        
    ob1=proffesor(name_institue)
    ob1.display()   
    print('*'*100,'\n')


#  lab assistant 
if choice =='2':

    print('*'*100,'\n')     
    qulification=(input("Enter the year of qulification = ")) 
    skill=input("What you have skill = ")     
    join=int(input("Year of joining = ")) 
    name_institue=input("Enter the name of institue = ")         
    ob2=lab_assistant( qulification,skill,join,name_institue,)
    ob2.display()
    print('*'*100,'\n')

# office assistant  
if choice =='3':
    print('*'*100,'\n') 
    qulification=(input("Enter the year of qulification = ")) 
    join=int(input("Year of joining = ")) 
    name_institue=input("Enter the name of institue = ")        
    ob3=office_assistant(qulification,join,name_institue)
    ob3.display()
    print('*'*100,'\n')

# peon
if choice =='4':
    print('*'*100,'\n')
    qulification=(input("Enter the year of qulification = ")) 
    join=int(input("Year of joining = ")) 
    name_institue=input("Enter the name of institue = ")        
    ob4=office_assistant(qulification,join,name_institue)
    ob4.display()