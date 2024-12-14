from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def description(self):
        print(f"This is a vehicle of brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print("Starting the car engine...")

    def stop_engine(self):
        print("Stopping the car engine...")

class MotorCycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print("Starting the motor cycle engine...")

    def stop_engine(self):
        print("Stopping the motor cycle engine...")


my_car = Car("Toyota", "Corolla")
my_motorcycle = MotorCycle("Kawasaki", "Ninja")
my_car.start_engine()
my_car.description()
my_motorcycle.stop_engine()
my_motorcycle.description()
