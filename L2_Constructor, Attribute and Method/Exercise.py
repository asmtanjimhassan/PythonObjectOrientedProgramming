class School:
    
    #non-parameterized constructor
    def __init__(self):
        print("Object Created")

WLFSC = School()
SJS = School()


class university:
    
    #parameterized constructor
    def __init__(self, name, number):
        self.name = name        #instance variable / data / attribute
        self.number = number    #instance variable / data / attribute

    #instance method
    def display(self):
        print("Object Created", self.name)

DU = university("DU", "3540")
BRAC = university("BRAC", "567")

DU.display()
BRAC.display()
