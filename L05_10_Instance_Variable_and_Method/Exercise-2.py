class House:
    def __init__(self):
        self.window = 4
        self.door = 2

    def view(self):
        print(self.window, "windows", self.door, "doors")

B23 = House()
B23.view()

B24 = House()
B24.door = 3
B24.view()
