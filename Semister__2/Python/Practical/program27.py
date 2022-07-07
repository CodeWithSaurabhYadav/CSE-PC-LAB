#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program that creates 26 text files named A.txt, B.txt, and up to Z.txt.
'''

import string as st

file_start_lst = list(st.ascii_uppercase)
for file_prefix in file_start_lst:
    file_name = file_prefix + ".txt"
    with open(f"outputfolder/{file_name}","w") as file:
        print(f"The file {file_name} created sucessfully.")