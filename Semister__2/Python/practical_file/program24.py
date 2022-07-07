#/bin/python3.10

'''
Write a python program to read and show first N lines to the user. The number of lines N will be taken from user input.
'''

print("Please enter file extension")
while True:
    try:
        try:
            file_name = input("Enter the file name : ")
            if file_name.endswith(".txt"):
                break
            else:
                print("Enter file name that ends with .txt")
        except Exception:
            print("Please enter valid input.")
    except KeyboardInterrupt:
        print("Please enter a value first and then enter.")


while True:
    try:
        try:
            reading_lines = int(input("Enter the number of lines you want to see : "))
            if reading_lines > 0:
                break
            else:
                print("Enter only natural numbers")
        except Exception:
            print("Please enter valid input.")
    except KeyboardInterrupt:
        print("Please enter a value first and then enter.")


with open(file_name,"r") as file:
    file_lines_list = file.readlines()

    print("\nThe particular lines are : \n")
    line = 0
    while reading_lines > line:
        print(f"{line+1}) {file_lines_list[line]}")
        line+=1
    file.close()
