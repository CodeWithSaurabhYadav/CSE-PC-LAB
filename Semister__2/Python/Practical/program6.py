#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program to implement basic arithmetic operations on user entered
numbers.
'''

# => functions

print("Calculator1")
star = 148
print("*"*star)
print('''
    1)Div
    2)Mul
    3)Add
    4)Sub
    ''')
print("*"*star)
while (True):
    try:
        operator = int(input("Enter operator : "))
        break
    except ValueError and NameError:
        print("You have entered wrong input for operator\n")
while (True):
    try:
        num1 = float(input("Enter number 1 : "))
        break
    except ValueError and NameError:
        print("You have entered wrong input for number 1\n")
while (True):
    try:
        num2 = float(input("Enter number 2 : "))
        break
    except ValueError and NameError:
        print("You have entered wrong input for number 1\n")

if operator == 1:
    ans = num1 / num2
    print("The div is : ",ans)
elif operator == 2:
    ans = num1 * num2
    print("The mul is : ",ans)
elif operator == 3:
    ans = num1 + num2
    print("The sum is : ",ans)
elif operator == 4:
    ans = num1 - num2
    print("The sub is : ",ans)
else:
    print("Invalid Operator")