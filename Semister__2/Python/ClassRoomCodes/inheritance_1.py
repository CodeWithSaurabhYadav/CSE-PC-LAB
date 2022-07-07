#/bin/python3.10

class person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        
class person_display(person):
    def display(self):
        print(self.name)
        print(self.surname)
        
# person1 = person("Saurabh","Yadav")
person1_display = person_display("Saurabh","Yadav")
person1_display.display()