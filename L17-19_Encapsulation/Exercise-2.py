class Student:
    def __init__(self, name, ID):
        self.name = name
        self.__ID = ID

    def details(self):
        print("Name:", self.name, "ID", self.__ID)

    """_________"""
    
    def set_name(self, name):
        if type(name) == str:
            self.name = name
        else:
            print("Inavlid Name. Enter again")

    def get_name(self):
        print(self.name)
  
    """_________"""
       
    def set_ID(self, ID):
        if (ID>0):
            self.__ID = ID
        else:
            print("Inavlid ID. Enter again")

    def get_ID(self):
        print(self.__ID)


s1 = Student("Rafiun", 11)
s2 = Student("Tanjim", 13)

s1.details()
s2.details()

s1.set_ID(34)
s1.get_ID()

s1.set_name("Faiza")
s1.get_name()
""" Conventional method for Encapsulation
-- Getter-setter method"""
