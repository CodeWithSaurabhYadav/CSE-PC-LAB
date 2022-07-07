#/bin/python3.10

'''
Write a python program to raise an exception with the python raise keyword
'''

num = 5
if num % 2 != 0:
    # if the condition above is true the below exception is raised
	raise Exception("The number shouldn't be an odd integer")