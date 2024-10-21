# 1
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print("Height is:", self.length)
        print("Width is:", self.width)
    
r1 = Rectangle(4, 3)
r1.display()
print("Area is", r1.area())

r2 = Rectangle(5, 3)
r2.display()
print("Perimeter is",r2.perimeter())

# 2
class Shape:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class Rectangle(Shape):
    def __init__(self, length, width, name):
        super().__init__(name)
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display(self):
        print("Type:", self.get_name())
        print("Height is:", self.length)
        print("Width is:", self.width)
    
r1 = Rectangle(4, 3, "Rectangle")
r1.display()
print("Area is", r1.area())

r2 = Rectangle(5, 3, "Rectangle")
r2.display()
print("Perimeter is",r2.perimeter())

# 3

class Shape:
    def __init__(self, name):
        self._name = name
        
    def __display_shape_type(self):
       print("Type:", self._name)
    
    def display_shape(self):
        self.__display_shape_type()

class Rectangle(Shape):
    def __init__(self, len, wid, name):
        Shape.__init__(self, name)
        self.__len = len
        self.__wid = wid
    
    def get_len(self):
        return self.__len
    
    def get_wid(self):
        return self.__wid
    
    def display(self):
        self.display_shape()
        print("Length:", self.get_len())
        print("Width:", self.get_wid())

r = Rectangle(4, 5, "Rectangle")
r.display()
    
     
