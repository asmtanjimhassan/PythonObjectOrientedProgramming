class Student:
    uni = "DU"
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def details(self):
        print(self.name, self.ID,
              Student.uni)

    @classmethod
    def updt_uni_name(cls, u_name):
        cls.uni = u_name

s1 = Student("Tanjim", 18)
s2 = Student("Rafiun", 4)

s1.details()

Student.updt_uni_name("Dhaka University")
# or s1.updt_uni_name("Dhaka University")

s1.details()

