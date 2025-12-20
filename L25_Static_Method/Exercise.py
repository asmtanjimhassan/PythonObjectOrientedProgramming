class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def details(self):
        print(self.name, self.ID)

    @staticmethod
    def check_dept(ID):
        if ID[3:5] == "01":
            print("CSE")
        elif ID[3:5] == "47":
            print("GEB")

s1 = Student("Tanjim", 18)

Student.check_dept("15347AB")
