#/bin/python3.10

'''
Write a python program that takes N number of integers from the user in a python list.
Create a function that takes the list of user entered numbers and returns MAX and MIN
numbers from that list to the user.
'''

# initilizing the content
lst = []

# min_max function for list items


def min_max(lst):
    lst.sort(reverse=True)
    return lst[len(lst)-1], lst[0]

def min_max_2(lst):
    min = lst[0]
    max = lst[1]
    for index in range(len(lst)):
        if min > lst[index]:
            min = lst[index]
        elif max < lst[index]:
            max = lst[index]
    return min,max

# Taking input from the user
for lst_index in range(int(input("Enter the no. of elements you want in the list : "))):
    while True:
        try:
            try:
                value = int(input("Enter the number : "))
                break
            except KeyboardInterrupt:
                print("\nExiting......\n")
                exit()
        except Exception as e:
            print("\nEnter Only numbers.\n")
    lst.append(value)

# taking min and max value of the list from min_max function
min, max = min_max(lst)

# Printing the min and max number of the list
print("Method 1")
print(f"The minimum number in the list is {min}")
print(f"The maximum number in the list is {max}")


# taking min and max value of the list from min_max function
min2, max2 = min_max_2(lst)

# Printing the min and max number of the list
print("\nMethod 2")
print(f"The minimum number in the list is {min2}")
print(f"The maximum number in the list is {max2}")