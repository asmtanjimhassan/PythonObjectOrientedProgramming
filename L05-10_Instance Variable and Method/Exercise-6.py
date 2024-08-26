class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self):
        print(self.color, "cat is", self.action)

    def compare(self, ct):
        if self.action == ct.action:
            print("Both cats are", self.action)
        else:
            print("Not really")

cat1 = Cat("Brown", "sitting")
cat2 = Cat("White", "sitting")

cat1.view()
cat2.view()

# pass by reference 
cat1.compare(cat2)
