#/binm/python3.10

'''
Demonstrate the use of basic string methods in python - lower(), upper(), join(), split(),
find(), and replace().
'''

from multiprocessing.sharedctypes import Value


text_string = "MY NAME IS XYZ. "

# lower()
print("lower() :",text_string.lower())

# Upper()
print("upper() :",text_string.upper())

# join()
lst = ["This","is","a","join()","function"]
print("join() :"," ".join(lst))

# Upper()
print("split() :",text_string.split())

# find()
text_string2 = "".join(text_string)
print("find() :",text_string2.find("xyz"))

# replace()
new_text = "I like bananas"
value = new_text.replace("bananas", "apples")
print(value)