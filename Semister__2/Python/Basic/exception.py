#/bin/python

#main program
while True:
    try:
        a = int(input("Enter the number : "))
        break
    except Exception as e:
        print("Invalid input",type(e))
    finally:
        print("This is finally statement")