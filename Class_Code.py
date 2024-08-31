class A:
      pass

# Python3 program to
# demonstrate instantiating
# a class
class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger1 = Dog()

Rodger1.attr1 = 'Bird'
Rodger1.attr2 = 'Sparrow'
print(Rodger1.attr1)
print(Rodger1.attr2)

Rodger2 = Dog()
Rodger2.attr1 = 'Animal'
Rodger2.attr2 = 'Human'
print(Rodger2.attr1)
print(Rodger2.attr2)

print(Rodger1.attr1)
print(Rodger1.attr2)
# Accessing class attributes
# and method through objects
#print(Rodger.attr1)
Rodger1.fun()
Rodger3 =Rodger2

# Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name
	

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Nikhil')

p.say_hi()






