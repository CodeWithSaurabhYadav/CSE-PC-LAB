f = open("FILE_1.txt", 'r')

lst = []
lst2 = []
lst3 = []
flag = True

while flag:
    num = f.readline()
    if num == '':
        print("EOF reached.")
        flag = False
    else:
        print("list appended.")
        lst.append(num)
for element in lst:
    lst2.append(element.strip())

for index in range(len(lst2)):
    lst3.append(int(lst2[index]))
print(lst)
print(lst2)
print(lst3)