# 1
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Product Name: {self.name}, Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail() 
        print(f"Warranty: {self.warranty}")

product = Product("Generic Product", 100)
product.display_detail()

electronic = ElectronicProduct("Smartphone", 999, "2 years")
electronic.display_detail()


# 2
class Shape:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __display(self):
        print(f"Shape: {self._name}")

    def display_info(self):
        print(f"Shape: {self._name}")

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def display_info(self):
        super().display_info() 
        print(f"Length: {self.__length}, Width: {self.__width}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")


shape = Shape("Generic Shape")
shape.display_info()

rectangle = Rectangle("Rectangle", 10, 5)
rectangle.display_info()

