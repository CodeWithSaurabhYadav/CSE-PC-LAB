#/bin/python3.10
# B-Tech Computer Science And Technology 
# Enro:- 202103103510362
# Name:- Saurabh Yadav

'''
Write a python program to demonstrate basic banking operations. Create a class named
banking having separate class methods for each operation. Call each method with an
instance of the class and attribute values to be taken from the user.
'''

class BankAccount:
    
    # Initial Function
    def __init__(self,AccNumber,AccHolder,AccBalance):
        self.AccNumber = AccNumber
        self.AccHolder = AccHolder
        self.AccBalance  = AccBalance 
    
    # Deposit Function
    def DepositBalance(self,DepositAmount):
        self.AccBalance+=DepositAmount
        print("*"*100)
        print("The Amount Credited.\nThe Account Balance is : ",self.AccBalance)
        
    # Withdrawal Function
    def WithdrawBalance(self,WithdrawAmount):
        if (WithdrawAmount > self.AccBalance):
            print("*"*100)
            print("You don't have enough balance.")
            print("*"*100)
        else:
            self.AccBalance-=WithdrawAmount
        print("*"*100)
        print("The Amount Debited.\nThe Account Balance is : ",self.AccBalance)
    
    # Displaying the details of the Account Holder
    def Display(self):
        print("*"*100)
        print("Account Number : ",self.AccNumber)
        print("Account Holder : ",self.AccHolder)
        print("Account Balance : ",self.AccBalance)
        
# Taking details of the Account Holder (Function)
def PersonDetails():
    while True:
        try:
            AccNum = int(input("Enter Account Nuimber : "))
            AccName = input("Enter Person Name : ")
            AccBal = float(input("Enter Account Balance : "))
            break
        except Exception:
            print("Invalid Details...\n")
    return AccNum,AccName,AccBal

# Storing the values of the Person in the below variables
AccNum1,AccName1,AccBal1 = PersonDetails()

# Person 1 Details
F_Person = BankAccount(AccNum1,AccName1,AccBal1)
# Person 1 Account Deposit
print("*"*100)
F_Person.DepositBalance(float(input("Enter Deposit Ammount : ")))
print("*"*100)
# Person 1 Account Withdraw
F_Person.WithdrawBalance(float(input("Enter Withdrawal Ammount : ")))

# displaying the Details for person 1
F_Person.Display()
print("*"*100)