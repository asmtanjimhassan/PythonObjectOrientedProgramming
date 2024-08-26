class calc:
    def __init__(self):
        pass

    def product(self, num1, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print(num1 * num2 * num3)
        elif num1 != None and num2 != None and num3 == None:
            print(num1 * num2)
        else:
            print(num1)


c1 = calc()
c1.product(4,5)
c1.product(5,6,7)

""" Method overloading - in same class, method with different parameters
We cant declare same method with different parameters in the same class"""

""" what if 4 parameters??"""


class calc1:
    def __init__(self):
        pass

    def product(self, *nums):
        pro = 1
        for x in nums:
            pro = pro * x
        print(pro)

c2 = calc1()
c2.product(4,5,6,7)

"""parameters are receieved as tuples."""
