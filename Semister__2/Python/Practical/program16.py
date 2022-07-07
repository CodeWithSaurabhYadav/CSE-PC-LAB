#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Create three classes named - C, Python, and Web_Designing each having two primary
attributes as learnings_ and name_of_professor. Derive a class named student from these
classes. The student class hase following methods and attributes:
   a. Global std_college attribute with static values.
   b. __init__() method with attributes - std_name, std_enrollment_no, and std_course.
   c. display() method to display various attribute values of the terminal.
'''

class c:
    def __init__(self,learnings,professor):
        self.learning_c = learnings
        self.professor_c = professor
class python:
    def __init__(self,learnings,professor):
        self.learning_p = learnings
        self.professor_p = professor
class web_designing:
    def __init__(self,learnings,professor):
        self.learning_w = learnings
        
        self.professor_w = professor

class student(c,python,web_designing):
    def __init__(self,enroll,name,course):
        self.enroll = enroll
        self.name = name
        self.course = course
        c.__init__(self,learnings_c,professor_c)
        python.__init__(self,learnings_python,professor_python)
        web_designing.__init__(self,learnings_web,professor_web)

    def display(self):
        print("")
        print("Enrollment number of student :",self.enroll)
        print("Name of the student :",self.name)
        print("Course :",self.course)
        print("Learnings :")
        print("C :",self.learning_c)
        print("Python :",self.learning_p)
        print("Web Designing :",self.learning_w)
        print("Professors :")
        print("C :",self.professor_c)
        print("Python :",self.professor_p)
        print("Web Designing :",self.professor_w)

def get_learnings(NumOfLearnings):
    learnings = []
    for amount in range(NumOfLearnings):
        learnings.append(input(f"Enter Learning {amount + 1} : "))
    return learnings
print("*"*100)
StudEnroll = input("Enter student enroll : ")
StudName = input("Enter student name :")
StudCourse = input("Enter student course :")

NumOfLearningsC = int(input("Enter number of learnings in C : "))
learnings_c = get_learnings(NumOfLearningsC)
professor_c = input("Enter professor name = ")

NumOfLearningsPython = int(input("Enter number of learnings in Python : "))
learnings_python = get_learnings(NumOfLearningsPython)
professor_python = input("Enter professor name = ")

NumOfLearningsWeb = int(input("Enter number of learnings in Web_Designing : "))
learnings_web = get_learnings(NumOfLearningsWeb)
professor_web = input("Enter professor name = ")


data1 = c(learnings_c,professor_c)
data2 = python(learnings_python,professor_python)
data3 = web_designing(learnings_web,professor_web)

student_obj = student(StudEnroll,StudName,StudName)
student_obj.display()