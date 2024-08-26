""" Object class is the parent class of all classes"""

class animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class dog(animal):
    def bark(self):
        print(self.name, "is barking")


a1 = animal("Rafiun")
d1 = dog("Efty")

d1.bark()
d1.eat()

a1.eat()

# a1.bark()

""" gives error. bark() method is not inherited by
animal class"""

# isinstance(Object, className)
print(isinstance(d1, animal))

# issubclass(Class, ClassName)
print(issubclass(animal, dog))
