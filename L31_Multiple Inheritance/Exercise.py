class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Method1")



class B:
    def __init__(self):
        print("__init__ of class B")

    def method1(self):
        print("Method2")


class C(A,B):
    #def __init__(self):
       # print("__init__ of class C")
       # __init__ method can be inherited from one of
       # the parent classes. which one?? A in this case

    #def __init__(self):
       #super().__init__()
       #print("__init__ of class C")

    #def __init__(self):
       #B.__init__(self)
    def method2(self):
        print("Method2")


c1 = C()
c1.method1()
B.method1(c1)
