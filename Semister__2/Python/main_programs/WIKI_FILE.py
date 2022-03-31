#/bin/python

from cgitb import text


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

# Main function to control the flow of the program
def main():
    file_name = input("Enter the text file name with extension(.txt) : ")
    searchable_txt = input("Enter the word you want to search : ").lower()
    text = extract_txt(file_name)
    # print(txt)
    count = counter(text,searchable_txt)
    
if __name__ == "__main__":
    main()