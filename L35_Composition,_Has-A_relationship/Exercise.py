class Engine:
    def __init__(self, cc):
        self.capacity = cc

    def start(self):
        print("Engine Started")

    def stop(self):
        print("Engine Stopped")


class Car(Engine):
    def __init__(self, brand, cc):
        self.brand = brand
        self.engine = Engine(cc)

    def run(self):
        self.engine.start()
        print("Car is running")


c1 = Car("BMW", 2000)

c1.run()
