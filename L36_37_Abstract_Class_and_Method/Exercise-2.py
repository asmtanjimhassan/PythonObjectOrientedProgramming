from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print("I am eating")


class Dog(Animal):
    def make_sound(self):
        print("Dog Barking")


class Cat(Animal):
    def make_sound(self):
        print("Meoww")

d1 = Dog()
d1.make_sound()

c1 = Cat()
c1.make_sound()
