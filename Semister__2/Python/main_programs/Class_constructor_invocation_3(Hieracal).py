# /bin/python3.10

class Parent:
    name1 = "Saurabh"
    name2 = "Rakesh"
    name3 = "Pradeep"


class Child_1(Parent):
    def display(self):
        print("Child_1 : ",self.name1)


class Child_2(Parent):
    def display(self):
        print("Child_2 : ",self.name2)


class Child_3(Parent):
    def display(self):
        print("Child_3 : ",self.name3)


obj1 = Child_1()
obj2 = Child_2()
obj3 = Child_3()

obj1.display()
obj2.display()
obj3.display()
