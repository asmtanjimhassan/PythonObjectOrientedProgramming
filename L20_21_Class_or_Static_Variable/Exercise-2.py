class Student:
    count = 0
    def __init__(self, name, ID):
        self.name = name      # instance variable
        self.ID = ID
        Student.count += 1
        
    def details(self):
        print(self.name, self.ID)

    def counter(self):
        print("Total: ", Student.count)


s1 = Student("Bob", 21)
s2 = Student("Mike", 23)
s3 = Student("Carol", 33)

s1.details()

s1.counter()

""" Every time an object is being created,
the constructor method is executed"""
