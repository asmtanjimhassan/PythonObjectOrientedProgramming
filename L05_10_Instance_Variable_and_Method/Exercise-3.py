class Car:

    def __init__(self, name, model):
        self.name = name       #instance variable
        self.model = model      #instance variable
        self.wheels = 4         #instance varaible

    def view(self):             #instance method
        print(self.name, " ", self.model, " ", self.wheels)

car1 = Car("BMW", 234)
car1.view()
