class student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def __str__(self):
        return "This is an Object " + self.name
        
s1 = student("Bob", 12)

print(s1)

""" when we print an object "s1" the __str__() is being called. """
