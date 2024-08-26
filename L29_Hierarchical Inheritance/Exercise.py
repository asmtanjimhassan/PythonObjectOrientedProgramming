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

class BBA(student):
    def party(self):
        print("all day party")

s1 = CSE("Rafiun", 19, 3)
s2 = BBA("Raiyan", 34)

s1.details()
s2.details()

s1.cry()
s2.party()
