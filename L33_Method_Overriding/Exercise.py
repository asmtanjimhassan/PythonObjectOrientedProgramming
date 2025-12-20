class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Always Study")

class B(A):
    def __init__(self):
        print("__init__ of class B")

    def method1(self):
        print("I cant study all day")

b1 = B()
b1.method1()
