#/bin/pyhton3.py

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