#/bin/pyhton3.py
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program to demonstrate the use of arbitrary arguments.
'''

# Arbitary Function
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Saurabh", "Rakesh", "Pradeep", "Manish")