class Animal(object):
	def __init__(self, name): #This is the constructor
		self.name = name

class Dog(Animal):
	num_legs = 4

	def __init__(self, name, breed): 
		super(Dog, self).__init__(name) # This calls the constructor of the super class, allows us to use name
		self.breed = breed #This is a unique attribute for the Dog class

	def speak(self):
		print("woof")

if __name__ == "__main__":
	a = Animal("Random")
	d = Dog("Doug", "Golden Retriever")
	d.speak()
	print(d.breed)