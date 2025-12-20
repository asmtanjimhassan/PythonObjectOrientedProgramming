class Student:
    def __init__(self, name, ID):
        self.name = name
        self.__ID = ID

        """ __ before variable encapsulates the variable"""

    def details(self):
        print("Name:", self.name, "ID", self.__ID)

    def update_ID(self, ID):
        if (ID>0):
            self.__ID = ID
        else:
            print("Inavlid ID. Enter again")


s1 = Student("Rafiun", 11)
s2 = Student("Tanjim", 13)

s1.ID = 66 #
print(s1.ID)

s1.__ID = 45 # It creates another instance variable (unnecessery)
print(s1.__dict__)


s1.details()
s2.details()

s1. update_ID(34)
s1.details()

""" Python doesn't have any keyword for public or private attribute.
Can't access properties within class"""
