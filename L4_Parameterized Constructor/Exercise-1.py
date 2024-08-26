class Student:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

        
        
s1 = Student("Rafiun", 11)
s2 = Student("Tanjim", 12)

"""any property of design class cannot be accessed without
reference of object"""

print(s1.name)

s1.ID = 24
print(s1.ID)
