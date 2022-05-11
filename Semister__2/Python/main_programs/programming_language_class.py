#/bin/python3.10

class c:
    def __init__(self,learnings,professor):
        self.learning = learnings
        self.professor = professor
class python:
    def __init__(self,learnings,professor):
        self.learning = learnings
        self.professor = professor
class web_designing:
    def __init__(self,learnings,professor):
        self.learning = learnings
        self.professor = professor

class student(c,python,web_designing):
    def __init__(self,enroll,name,course):
        self.enroll = enroll
        self.name = name
        self.course = course
        c.__init__(self,learnings,professor)
        python.__init__(self,learnings,professor)
        web_designing.__init__(self,learnings,professor)


print("*"*100)
NumOfLearningsC = int(input("Enter number of learnings in c : "))
learnings = []
for amount in range(NumOfLearningsC):
    learnings.append(input(f"Enter Learning {amount} : "))
professor=input("Enter professor name = ")
StudEnroll = input("Enter student enroll : ")
StudName = input("Enter student name :")
StudCourse = input("Enter student course :")

NumOfLearningsPython = int(input("Enter number of learnings in c : "))
learnings = []
for amount in range(NumOfLearningsPython):
    learnings.append(input(f"Enter Learning {amount} : "))
professor=input("Enter professor name = ")
StudEnroll = input("Enter student enroll : ")
StudName = input("Enter student name :")
StudCourse = input("Enter student course :")

NumOfLearningsWeb = int(input("Enter number of learnings in c : "))
learnings = []
for amount in range(NumOfLearningsWeb):
    learnings.append(input(f"Enter Learning {amount} : "))
professor=input("Enter professor name = ")
StudEnroll = input("Enter student enroll : ")
StudName = input("Enter student name :")
StudCourse = input("Enter student course :")

data1 = c(learnings,professor)
data2 = python(learnings,professor)
data3 = web_designing(learnings,professor)
print('*'*100,'\n')