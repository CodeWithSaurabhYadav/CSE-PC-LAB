#/bin/python3.10

'''
Write a python program that takes input of a student course from the user and and write it in a file.
'''

while True:
    try:
        try:
            count = int(input("Enter the number of courses you want to add : "))
            if count > 0:
                break
            else:
                print("Enter only natural numbers")
        except Exception:
            print("Please enter valid input.")
    except KeyboardInterrupt:
        print("Please enter a value first and then enter.")

index_count = 0
course_list = []
while count > index_count:
    course_list.append(input(f"Enter course {index_count+1} name : "))
    index_count+=1

with open("program25.txt","w") as course_file:
    for index in range(len(course_list)):
        course_file.write(f"Course {index+1} : {course_list[index]}\n")
    course_file.close()

print("The course names are saved into program25.txt file")