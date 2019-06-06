class Animal(object):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    num_legs = 4

    # Constructor
    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed

    def speak(self):
        print("woof");

if __name__ == "__main__":
    d = Dog("Doug", "golden retriever")
    d.speak()
    print(d.breed)
    print(d.name)
    print(d.num_legs)
