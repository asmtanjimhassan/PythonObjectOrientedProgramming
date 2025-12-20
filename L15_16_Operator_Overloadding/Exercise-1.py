class myway:
    def __init__(self, x, y):
        self.sum = x+y

num1 = myway(4,5)
num2 = myway(10,2)

print(num1.sum+num2.sum)


class data:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
        

num3 = data(12)
num4 = data(20)

str1 = data("CSE")
str2 = data("110")

print(num3 + num4) # num3.__add__(num4)
print(str1 + str2)
