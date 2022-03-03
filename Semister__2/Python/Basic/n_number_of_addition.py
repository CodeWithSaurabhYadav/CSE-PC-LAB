#/bin/python3

#Functions for calculation
# Odd even function
def EvenOdd(num):
    lst = []
    for i in range(len(num)):
        if num[i]%2 == 0:
            lst.append("Even")
        else:
            lst.append("Odd")
    return lst
# Sum function
def sum(x):
    answer = x[0]
    for i in range(1,len(x)):
        answer+=x[i]
    return answer
# Subtraction Function
def difference(x):
    answer = x[0]
    for i in range(1,len(x)):
        print(x[i])
        answer-=x[i]
    return answer
# Multiplication Function    
def product(x):
    answer = x[0]
    for i in range(len(x)):
        answer*=x[i]
    return answer
# Division Function
def divide(divident,divisor):
    answer = divident/divisor
    return answer

#Input the numbers
def enter(num_num):
    lst = []
    for i in range(0,num_num):
        item = int(input(f"Enter the number {i+1} : "))
        lst.append(item)
    return lst

#Main function
def main():
    print("-"*45)
    print('''
        1) Addition
        2) Subtraction
        3) Multiplication
        4) Division
        5) Odd-Even
        ''')
    print("-"*45)
    choice = int(input("Enter yor choice(1-4) : "))
    if choice == 1:
        num_num = int(input("\nEnter the number of numbers you want to add : "))
        num_lst = enter(num_num)
        print(f"The sum of your entered numbers is {sum(num_lst)} .")
    elif choice == 2:
        num_num = int(input("\nEnter the number of numbers you want to subtract : "))
        num_lst = enter(num_num)
        print(f"The difference of your entered numbers is {difference(num_lst)} .")
    elif choice == 3:
        num_num = int(input("\nEnter the number of numbers you want to multiply : "))
        num_lst = enter(num_num)
        print(f"The product of your entered numbers is {product(num_lst)} .")
    elif choice == 4:
        num1 = int(input("Enter Divident : "))
        num2 = int(input("Enter Divisor : "))
        print(f"The dividion of your entered numbers is {divide(num1,num2)} .")
    elif choice == 5:
        num_num = int(input("\nEnter the number of numbers you want to check : "))
        num_lst = enter(num_num)
        check_lst = EvenOdd(num_lst)
        # print(check_lst[0])
        for i in range(len(num_lst)):
            print(f"The number {num_lst[i]} is {check_lst[i]}.")
    else:
        print("You Have etered wrong input.")
        
# If name and main conditional statement
if __name__ == "__main__":
    main()
