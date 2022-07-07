#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program to demonstrate the creation of a Dictionary student with the
name, age and branch of a student.
    a. Demonstrate the updation of python dictionary.
    b. Demonstrate the removal of elements from the python dictionary.
    c. Demonstrate the use of following dictionary methods - clear(), copy(), get(),
    items(), keys(), popitem(), and values().
'''

# Creation of the dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("This is a dictionary :",thisdict)

# (a) Updation of the dictionary
thisdict2 = {
    "batch no.": "A42DFS"
}
thisdict.update(thisdict2)
print("This is the updation of the dictionary :",thisdict)

# (b) Removal of the elements of the dictionary
thisdict.pop("model")
print("The modal element is removed from the dictionary :",thisdict)

# (a) clear(), copy(), get(), items(), keys(), popitem(), and values().
thisdict2.clear()
print("The dictionary 2 is now cleared :",thisdict2)
thisdict3 = thisdict.copy()
print("The dict3 is a copy of the dict 1:",thisdict3)
print("get() function :",thisdict.get("year"))
print("items() function :",thisdict.items())
print("keys() function :",thisdict.keys())
thisdict.popitem()
print("popitem() function :",thisdict)