class ABC:
    def __init__(self, x, y):
        self.x = x
        self.__y = y # private instance variable

    def details(self):
        print(self.x, self.__y)
        self.__method()

    def __method(self):
        print("Private Method Executed")

a1 = ABC(5,6)
a2 = ABC(3,4)

a1.details()

# a1.__method() # it cannot be accessed


