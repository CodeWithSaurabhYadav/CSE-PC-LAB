#/bin/python3

num1 = int(input("Enter the number : "))

if num1 > 0:
    print(num1,"is greater than 0.")
elif num1 == 0:
    print(num1,"is equal to 0.")
elif num1 < 0:
    print(num1,"is smaller than 0.")
else:
    print("None")