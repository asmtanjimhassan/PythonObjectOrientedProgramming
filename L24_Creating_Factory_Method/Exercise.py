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

    @classmethod
    def from_string(cls, info):
        name, ID = info.split('-')
        obj = Student(name, ID)
        return obj

s1 = Student("Tanjim", 18)
s2 = Student.from_string("Rafiun-4")

s1.details()
s2.details()

