#/bin/python3.10

# This is a Parent Class (Base Class)
class ParentClass:
    name = "Saurabh"
    
# The Below Class is child (Derived from) of ParentClass 
class ChildClass_1(ParentClass):
    surname = "Yadav"

# The Below Class is not a child (Not Derived from) of ParentClass 
class ChildClass_2:
    age = 18

print()
# This will give output as true because ChildClass_1 is derived from ParentClass
print("Parent Class and Child class 1")
print(issubclass(ChildClass_1,ParentClass))
print()
# This will give output as false because ChildClass_2 is not derived from ParentClassx
print("Parent Class and Child class 2")
print(issubclass(ChildClass_2,ParentClass))