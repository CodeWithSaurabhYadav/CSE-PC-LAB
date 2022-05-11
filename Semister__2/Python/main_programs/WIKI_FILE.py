#/bin/python


# def all_in_one(file_n,txt):
#     with open(file_n,"r") as file:
#         counter_num = file.read().lower().count(txt)
#         file.close()
#         return counter_num

def extract_txt(file_name):
    # This reads the lines of the text file
    with open(file_name,"r") as file:
        text = file.read()
        return text.lower()

# This counts the number of the times the word has been found in the text file.
def counter(wiki_lst,searchable):
    count = wiki_lst.count(searchable)
    if count == 0:
        print("The word not found in the text file you entered.")
    else:
        print("The word {0} occured {1} times in the text file you entered.".format(searchable,count))

def global_finder(text):
    def make_list(file_name):
        # This reads the lines of the text file
        with open(file_name,"r") as file:
            lst = file.readlines()
        
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
        return lst,count_lst

    # Main function to control the flow of the program
    def check():
        lst = make_list(text)
        element,value = counter(lst)
        for element_index in range(len(element)):
            print(element[element_index],":",value[element_index])
        main()
    check()
# Main function to control the flow of the program
def main():
    print('''
          Your choices :
          1) Find text
          2) Global
          3) Exit
          ''')
    while True:
        try:
            try:
                choice = int(input("choice : "))
                break
            except Exception as e:
                print("Enter correct input")
            if choice == 1:
                file_name = input("Enter the text file name with extension(.txt) : ")
                searchable_txt = input("Enter the word you want to search : ").lower()
                text = extract_txt(file_name)
                count = counter(text,searchable_txt)
            elif choice == 2:
                file_name = input("Enter the text file name with extension(.txt) : ")
                global_finder(file_name)
            elif choice == 3:
                print("Thanks for using the program.\nExiting.......")
                exit()
            else:
                print("Invalid input!!! Please enter choice form above only")
                main()
        except KeyboardInterrupt:
            print("The entered choice is in valid.")
            main()
    
if __name__ == "__main__":
    main()
