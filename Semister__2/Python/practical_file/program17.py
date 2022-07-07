#/bin/python3.10

'''
Write a python program to demonstrate the use of data hiding
'''

class Base():
    # Below is hidden classVariable
    __ThisIsHidden = "I am a Hidden Varaible"
    ThisIsNotHidden = "I am not a Hidden Varaible"

obj = Base()
print(obj.ThisIsNotHidden)

# The below statement will give an AttributeError as __ThisIsHidden is hidden inside the Base() Class
print(obj.__ThisIsHidden())