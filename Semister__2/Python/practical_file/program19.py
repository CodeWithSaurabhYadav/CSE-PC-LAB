#/bin/pyhton3.10

'''
Write a python program to demonstrate the use of the method overriding
'''

class Parent():
	
	def __init__(self):
		self.value = "Inside from Parent"

	def show(self):
		print(self.value)
		
class Child(Parent):

	# As soon as a function or attribute is defined in the child it is overridden by it
	def __init__(self):
		self.value = "Inside from Child"
		
	def show(self):
		print(self.value)
		
		

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
