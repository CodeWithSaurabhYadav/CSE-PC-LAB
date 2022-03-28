'''
# This part of code is just for writng random 100 numbers into the file
import random as rd

with open("FILE_1.txt","w") as file:
    for i in range(100):
        file.write(str(rd.randint(-100,100)))
        file.write("\n")
'''
#This is to make list from file
def file_list_creator():
    with open("FILE_1.txt","r") as file:
        str_lst = file.readlines()  #This gives us srting list with '\n' at the end of each number
    no_str_lst = []
    for element in str_lst:
        no_str_lst.append(int(element.strip())) #Using strip function we change the element of str_lst to integer values
    return no_str_lst   #This is the integer list that we are returning

#Finding and returning min and max values from lst extracted from file
def min_max_lst(lst):
    lst.sort()
    return lst[0],lst[len(lst)-1] #returning min,max value using indexing

#This is just a main function
def main():
    lst = file_list_creator()
    min,max = min_max_lst(lst)
    print("The max number is {0}".format(max))
    print("The min number is {0}".format(min))

main()
