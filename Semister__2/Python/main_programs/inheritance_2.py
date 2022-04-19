from unicodedata import name


class base:
    Fname = "Saurabh"
    def printfun(self):
        print("Name :",self.Fname)
        
class derived(base):
    Lname = "Yadav"
    def printfun(self):
        print("Name :",self.Fname)
    
class secound_derived(derived):
    def printfun(self):
        print("Name :",self.Fname,self.Lname)
        
obj = secound_derived()
obj.printfun()