#/bin/python
'''
# This is for write random 100 number in a file.
import random as rd
file_obj = open("FILE_1.txt","w")
for i in range(100):
    number = rd.randint(-100,100)
    file_obj.write(f"{number}\n")
file_obj.close()
'''

# This is file method file
from pexpect import EOF


class FILE_NUMBER():
    def max_min_from_file(number_lst):
        min = number_lst[0]
        max = number_lst[1]
        number_lst.sort(reverse=True)
        return number_lst[len(number_lst)-1], number_lst[0]
    def file_number_list(file):
        number_lst = []
        with open(file,"r") as file:
            # Initilizing the list for our operation
            main_lst = []
            striped_lst = []
            number_lst = []
            flag = True
            # Creating the list from file
            while flag:
                num = file.readline()
                if num == '':
                    # print("EOF reached.")
                    flag = False
                else:
                    # print("list appended.")
                    main_lst.append(num)
            # Removing the newline character from the list
            for element in main_lst:
                striped_lst.append(element.strip())

            # Converting the files into integer
            for index in range(len(striped_lst)):
                number_lst.append(int(striped_lst[index]))
        return number_lst
# Main Program
def main():
    file_name = input("Enter file name (ONLY TXT) with extension : ")
    number_lst = FILE_NUMBER.file_number_list(file_name)
    # print(number_lst)
    min,max = FILE_NUMBER.max_min_from_file(number_lst)
    print()
    print("The Maximum number in the file is :",max)
    print("The Minimum number in the file is :",min)
    
if __name__ == "__main__":
    main()