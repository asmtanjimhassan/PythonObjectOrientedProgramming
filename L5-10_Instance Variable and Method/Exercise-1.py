class Student:

    def __init__(self, name, ID):
        self.name = name # instance variable
        self.ID = ID     # instance variable
        
    # Instance method
    def details(self):
        print("Name", self.name, "ID", self.ID)
        
        
s1 = Student("Rafiun", 11)
s2 = Student("Tanjim", 12)

s1.details()

