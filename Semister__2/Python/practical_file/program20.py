#/bin/python3.10

'''
Write a python program to demonstrate the use of try-catch block for exception handling
'''

try:
    int_val = int(input("Enter any  : "))
    print("The Value is an integer value")
except Exception:
    print("The value is not an integer")