class student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def details(self):
        print(self.name, self.ID)

class CSE(student):
    def __init__(self, name, ID, labs):
        super().__init__(name, ID)
        self.no_of_labs = labs

    def cry(self):
        print("CSE students always cry")

class CSEFresher(CSE):
    def enroll_110(self):
        print("Enrolled in CSE110")

s1 = CSEFresher("Rafiun", 19, 3)
s2 = CSE("Tanjim", 18, 5)

s1.details()
s1.cry()
s1.enroll_110()

# s2.enroll_110() gives error
