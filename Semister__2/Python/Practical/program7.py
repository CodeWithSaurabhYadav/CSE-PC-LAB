#/bin/pyhton3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program to count how many times a specific number is occurring in a list.
Take user input for both numbers and a list.
'''

def input_list(ele_num):
    lst = []
    for element in range(ele_num):
        while True:
            try:
                try:
                    lst.append(int(input("Enter :")))
                    break
                except Exception:
                    print("Enter only number.")
            except KeyboardInterrupt:
                print("Enter the value to complete the list.\n")
    return lst


def main():
    ele_num = int(input("Enter the number of elements in list : "))
    lst = input_list(ele_num)
    while True:
        try:
            try:
                searchable = int(input("Enter the number you want to count : "))
                break
            except Exception:
                print("Enter only number")
        except:
            print("Enter value first.")

    print(f"The number {searchable} has occured {lst.count(searchable)} times in the entered list.")

main()