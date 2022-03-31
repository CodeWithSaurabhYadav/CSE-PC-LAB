#/bin/python3

def comapare(lst1,lst2):
    lst = []
    count_lst = []
    for index_1 in range(len(lst1)):
        for index_2 in range(len(lst1)):
            for index_3 in range(len(lst2)):
                if lst1[index_1] == lst1[index_2] or lst1[index_1] == lst2[index_3]:
                    if lst1[index_1] not in lst and lst1[index_1] in lst2:
                        lst.append(lst1[index_1])
                        
    for num_count in range(len(lst)):
        val = lst1.count(lst[num_count]) + lst2.count(lst[num_count])
        count_lst.append(val)
    return lst,count_lst

def input_list(ele_num):
    lst = []
    for element in range(ele_num):
        lst.append(input("Enter :"))
    return lst

def main():
    ele_num = int(input("Enter the number of elements of list 1 : "))
    lst1 = input_list(ele_num)
    ele_num = int(input("Enter the number of elements of list 2 : "))
    lst2 = input_list(ele_num)
    
    val_lst,num_lst = comapare(lst1,lst2)
    print("The number of times is :\nElement : Number of times it occur")
    for index in range(len(val_lst)):
        print("{0} : {1}".format(val_lst[index],num_lst[index]))

if __name__ == "__main__":
    main()