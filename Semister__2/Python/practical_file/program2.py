#/bin/python3.10

'''
Write a python program to demonstrate the creation of List data structure along with its
methods - append(), extend(), insert(), remove(), clear(), index(), count(), sort(),
reverse(), and copy().
    a. Demonstrate positive and negative indexing with python List.
    b. Demonstrate slicing operations on python List.
    c. Demonstrate updation on List elements in python.
    d. Demonstrate deletion of a single python list element and multiple elements using slicing operator
'''

# Creation of list data structure
lst = [1,2,3,4,5,6,7]
print(lst)

# List data structure methods

lst.append(8)      # lst_name.append(value)
print("Append :",lst)

lst2 = [9,10]
print(lst2)
lst.extend(lst2)    # lst_name.extend(another_lst)
print("Extend :",lst)

lst.insert(0,0)     # lst_name.extend(index,value)
print("Insert :",lst)

lst.remove(10)      # lst_name.remove(value_to_remove)
print("Remove",lst)

lst2.clear()         # Accepts no argument but clears the entire list -- lst_name.clear()
print("Clear :",lst2)

print("Index: ",lst.index(5))         # lst_name.index(value_to_get_index)

print("Count :",lst.count(3))         # lst_name.count(value_to_count)

lst.sort()      # Arranges the entire list item in assending order -- lst_name.sort()
print("Sort :",lst)

lst.reverse()      # Arranges the entire list item in decending/reverse order -- lst_name.reverse()
print("Reverse :",lst)

lst3 = lst.copy()
print("Copy :",lst3)

print()
print()

# a. Demonstrate positive and negative indexing with python List.
large_lst = [1,23,133,3321,4,84]

print("Positive Indexing")
for i in range(len(large_lst)):
    print(large_lst[i])

print("Negative Indexing")
count = len(large_lst) - 1
while count >= 0:
    print(large_lst[count])
    count-=1

# b. Demonstrate slicing operations on python List.
print("Slicing Operation")
print(large_lst[2:5])

# c. Demonstrate updation on List elements in python.
print("Updation on list element")
large_lst[0] = 43434
print(large_lst)

# d. Demonstrate deletion of a single python list element and multiple elements using slicing operator
print("Single element deletion from list")
large_lst.pop(3)
print(large_lst)

print("Multiple element deletion from list")
del(large_lst[3:5])
print(large_lst)