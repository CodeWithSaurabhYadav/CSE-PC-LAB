import os
from random import randint as rd


for i in range(1,500):
    for j in range(0,rd(0,7)):
        date = str(i) + 'days age'
        with open("file.txt","a") as file:
            file.write(date + "\n")
        os.system("git add .")
        os.system('git commit --date="' + date + '" -m "updating the previous changes commits"')

os.system("rm app.py")
os.system("rm file.txt")
os.system("git add .")
os.system('git commit -am "Savin the content of the files"')