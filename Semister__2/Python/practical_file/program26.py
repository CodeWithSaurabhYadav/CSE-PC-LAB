#/bin/python3.10

'''
Write a python program to copy the content of one file to another file.
'''


def get_files():
    lst = ["source","destination"]
    file_name_lst = []
    print("Please enter file extension")
    for file_name_number in range(2):
        while True:
            try:
                file_name = input(f"Enter the {lst[file_name_number]} file name : ")
                if file_name.endswith(".txt"):
                    file_name_lst.append(file_name)
                    break
                else:
                    print("The file must be a text file")
            except KeyboardInterrupt:
                print("Enter file name and then enter.")
    return file_name_lst[0],file_name_lst[1]

# Taking Source file name and Destination file name
src_file_name,dec_file_name = get_files()

with open(src_file_name,"r") as src_file:
    src_content = src_file.readlines()
    with open(dec_file_name,"w") as dec_file:
        for line in src_content:
            dec_file.write(line)
    src_file.close()
    dec_file.close()

print(f"The content of the file {src_file_name} is copied to {dec_file_name}.")