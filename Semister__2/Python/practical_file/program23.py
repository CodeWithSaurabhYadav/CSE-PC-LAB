#.bin/python3.10

'''
Write a python program to read the content of a file and return the number of
words in a file to the user
'''

from secrets import choice
from tkinter import N
from traceback import print_tb


def global_finder(text):
    def make_list(file_name):
        # This reads the lines of the text file
        try:
            with open(file_name, "r") as file:
                lst = file.readlines()
        except Exception:
            print(f"Unable to locate file {file_name}.")
            main()

        # This removes spaces between the elements and appends it into lst2
        lst2 = []
        for i in lst:
            lst2.append(i.split())

        # This takes the individual elements form lst2 and extend the lst3
        lst3 = []
        for fin_ele in lst2:
            lst3.extend(fin_ele)

        # This removes any extra character like .,\"\"() from any element in the list3
        lst4 = []
        for clear_txt_ele in lst3:
            lst4.append(clear_txt_ele.strip(".,\"\" ()"))

        # This converts the list4 elements into lower case characters
        lst5 = []
        for lower_ele in lst4:
            lst5.append(lower_ele.lower())

        # This returns the list5
        return lst5

    # This simply scans the list and returns common string with the other list containing
    # the number of times the element has occured in the list.
    def counter(wiki_lst):
        lst = []
        count_lst = []
        for index_1 in range(len(wiki_lst)):
            for index_2 in range(len(wiki_lst)):
                if wiki_lst[index_1] == wiki_lst[index_2]:
                    if wiki_lst[index_1] not in lst:
                        lst.append(wiki_lst[index_1])

        for num_count in range(len(lst)):
            count_lst.append(wiki_lst.count(lst[num_count]))
        return lst, count_lst

    # Main function to control the flow of the program
    def check():
        lst = make_list(text)
        element, value = counter(lst)
        for element_index in range(len(element)):
            print(element[element_index], ":", value[element_index])
        while True:
            try: 
                choice = input("Do you want to continue (Y/N): ")
                break
            except Exception:
                print("\nEnter a valid input and then enter")
        if choice == 'N' or choice == "n":
            print("Exiting the program.")
            exit()
        else:
            main()
    check()


# Main function to control the flow of the program
def main():
    print("\nPlease enter file extension")
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
    try:
        global_finder(file_name)
    except Exception:
        print("Unable to locate file.")
if __name__ == "__main__":
    main()