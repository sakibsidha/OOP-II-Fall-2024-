class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicleInfo(self):
        return f"Vehicle Color: {self.color}"


class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self.__model = model 
        self.__capacity = capacity
        self.__variant = variant  

    # Getters
    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

    # Setters
    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    def vehicleInfo(self):
        parent_info = super().vehicleInfo()
        return (f"{parent_info}, Model: {self.__model}, "
                f"Capacity: {self.__capacity}, Variant: {self.__variant}")


t1 = Taxi("Red", "Sedan", 4, "Petrol")
t2 = Taxi("Yellow", "SUV", 7, "Diesel")

print(t1.vehicleInfo())
print(t2.vehicleInfo())

# Updating attributes using setters
t1.setModel("Hatchback")
t1.setCapacity(5)
t1.setVariant("Electric")

print("\nAfter updating t1 details:")
print(t1.vehicleInfo())
