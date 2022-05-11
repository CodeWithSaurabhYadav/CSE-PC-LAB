#.bin/python3.10

'''
Write a python program to read the content of a file and return the number of
words in a file to the user
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

with open(file_name,"r") as file:
    NumOfLines = len(file.readlines())
    print(f"The particular {file.name} contains {NumOfLines} number of lines.")
    file.close()