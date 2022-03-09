#/bin/python

# initilizing the content
lst = []

# min_max function for list items
def min_max(lst):
    lst.sort(reverse=True)
    return lst[len(lst)-1],lst[0]

# Taking input from the user
for lst_index in range(10):
    while True:
        try:
            value = int(input("Enter the number : "))
            break
        except Exception as e:
            print("\nEnter Only numbers.\n")
    lst.append(value)

# taking min and max value of the list from min_max function
min,max = min_max(lst)

# Printing the min and max number of the list 
print(f"The minimum numbe in the list is {min}")
print(f"The maximum numbe in the list is {max}")