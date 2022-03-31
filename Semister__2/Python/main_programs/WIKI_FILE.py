#/bin/python

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
def main():
    file_name = "WIKI.txt"
    lst = make_list(file_name)
    print(lst)
    element,value = counter(lst)
    print(element)
    print(value)
if __name__ == "__main__":
    main()