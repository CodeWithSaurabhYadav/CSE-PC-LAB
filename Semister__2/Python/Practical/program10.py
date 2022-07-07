#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

''''
Write a python program to perform basic operations of a calculator. Provide choice for
operations to users and make a program iterative. Provide specific exit option to users.
'''


# basic function for arithmeatic operations
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2


# function to take input
def input_function():
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
    return float(num1),float(num2)


# main loop of a program
def main():
    star = 148
    print("*"*star)
    print('''
        1) Div
        2) Mul
        3) Add
        4) Sub
        5) Exit
        ''')
    print("*"*star)
    while (True):
        try:
            operator = int(input("Enter operator : "))
            break
        except ValueError and NameError:
            print("You have entered wrong input for operator\n")
    if operator == 1:
        num1,num2 = input_function()
        ans = div(num1,num2)
        print("The div is : ",ans)
        main()
    elif operator == 2:
        num1,num2 = input_function()
        ans = mul(num1,num2)
        print("The mul is : ",ans)
        main()
    elif operator == 3:
        num1,num2 = input_function()
        ans = add(num1,num2)
        print("The sum is : ",ans)
        main()
    elif operator == 4:
        num1,num2 = input_function()
        ans = sub(num1,num2)
        print("The sub is : ",ans)
        main()
    elif operator == 5:
        print("Thanks for using.")
        exit()
        
if __name__ == "__main__":
    main()