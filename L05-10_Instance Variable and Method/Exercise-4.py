class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name)

d1 = Dog("rover", "Brown")
d2 = Dog("Bogo", "Black")

d1.poke()
d2.poke()

d1.update_color("White")
d1.poke()

print(d1.__dict__)

# exhibits all the built in properties
print(dir(d1))
