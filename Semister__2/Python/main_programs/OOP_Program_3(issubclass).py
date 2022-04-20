#/bin/python3.10

class ParentClass:
    name = "Saurabh"
    
class ChildClass_1(ParentClass):
    surname = "Yadav"
    
class ChildClass_2:
    age = 18

print()
print("Parent Class and Child class 1")
print(issubclass(ChildClass_1,ParentClass))
print()
print("Parent Class and Child class 2")
print(issubclass(ChildClass_2,ParentClass))
