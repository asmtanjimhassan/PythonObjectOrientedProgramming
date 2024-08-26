class Animal:
    def __init__(self, name):
        self.name = name
        self.color = "white"

    def eat(self):
        print(self.color, self.name, "is eating")

class dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        
    def bark(self):
        print(self.color, self.name, "is eating")

d1 = dog("Rover", "Brown")
d1.bark()

d1.eat()
