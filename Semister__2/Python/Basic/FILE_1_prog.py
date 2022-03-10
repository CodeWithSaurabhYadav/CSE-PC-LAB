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
class FILE_NUMBER():
    def max_min_from_file(number_lst):
        min = number_lst[0]
        max = number_lst[1]
        for index in range(len(number_lst)):
            if min > number_lst[index]:
                min = number_lst[index]
            elif max < number_lst[index]:
                max = number_lst[index]
        return min,max
    def file_number_list(file):
        number_lst = []
        with open(file,"r") as file:
            file.seek(0)
            print(type(file))
            for line in range(5):
                value = int(file.readline())
                number_lst.append(value)
        return number_lst
# Main Program
def main():
    file_name = input("Enter file name (ONLY TXT) with extension : ")
    number_lst = FILE_NUMBER.file_number_list(file_name)
    print(number_lst)
    min,max = FILE_NUMBER.max_min_from_file(number_lst)
    print()
    print("The Maximum number in the file is :",max)
    print("The Minimum number in the file is :",min)
    
if __name__ == "__main__":
    main()