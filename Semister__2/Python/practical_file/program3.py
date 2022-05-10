#/bin/pyton3.10

'''
Write a python program to demonstrate the creation of tuples along with its methods -
count() and index().
    a. Demonstrate positive and negative indexing with python Tuple.
    b. Demonstrate slicing operations on python Tuple.
    c. Demonstrate updation on Tuple elements in python.
''' 

# creation of tuples
tup1 = (1,2,3,4,5,2,2)
print("This is a tuple : ",tup1)

# count() method of tuple
print("This is a tuple.count() program : ",tup1.count(2))

# index() method of tuple
print("This is a tuple.index() program : ",tup1.index(2))

# (a) +ve indexing of tuple
print("This is positive indexing of tuple :",tup1[5])

# (a) -ve indexing of tuple
print("This is negative indexing of tuple :",tup1[-5])

# (b) slicing of the tuple
print("This is a slicing of the tuple :",tup1[2:5])

# (c) updation of the tuple elements
tup1 = list(tup1)
print("The tuple is converted to list so that it can be updarted.", tup1)
tup1[5] = 25
tup1 = tuple(tup1)
print("The list is updated and converted back to tuple :",tup1)