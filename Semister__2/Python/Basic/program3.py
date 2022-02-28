#list For Loop
lst = []
print("List using for loop: \n")
for i in range(1,30,5):
    lst.append(i)

for j in range(len(lst)):
    print(lst[j])
    
#Dict For Loop
print("\nDictionary using for loop: \n")
dict = {"Name":"saurabh","age":18,"College":"AMTICS","Student-Year":"Second"}
for key,val in dict.items():
    print(key,":",val)
    
#List While
print("List using for loop: \n")
k = 0
while (k < (len(lst)-1)):
    k+=1
    print(lst[k])
    
#Dict While Loop
print("\nDictionary using while loop: \n")
dict = {"Name":"saurabh","age":18,"College":"AMTICS","Student-Year":"Second"}
key2 = 0
while (len(dict)):
    print(dict.keys())
    print(dict.values())
    key2+=1
