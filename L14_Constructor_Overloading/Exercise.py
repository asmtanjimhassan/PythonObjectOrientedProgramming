class student:
    def __init__(self, *info):
        if len(info) == 3:
            self.name = info[0]
            self.ID = info[1]
            self.cg = info[2]

        elif len(info) == 2:
            self.name = info[0]
            self.ID = info[1]
        elif len(info) == 1:
            self.name = info[0]

        print("An Object Created")

s1 = student("Carol", 33, 3.92)
s2 = student("Bob", 54, 4.00)
s3 = student("Mike")

""" If same class has multiple init method, it is Constructor Overloading"""

class student1:
    def __init__(self, **info):
        if len(info) == 3:
            self.name = info['name']
            self.ID = info['ID']
            self.cg = info['cg']

        elif len(info) == 2:
            self.name = info['name']
            self.ID = info['ID']
        elif len(info) == 1:
            self.name = info['name']

        print(self.name)

s4 = student1(name = "Carol", ID = 33, cg = 3.92)
s5 = student1(name = "Bob", ID = 54, cg = 4.00)
s6 = student1(name = "Mike")


class my_way:
    def __init__(self, *info):
        self.info = []
        for x in info:
            self.info.append(x)

        print(self.info)

s7 = my_way("Mike", 34, 3.92)
