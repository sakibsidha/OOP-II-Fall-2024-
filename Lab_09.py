# 1
class InvalidAgeExecption(Exception):
    pass

try:
    age = int(input())
    if (age < 18):
        raise InvalidAgeExecption
    print("Age:", age)
except InvalidAgeExecption:
    print("Invalid Age Exception Occured!")
except:
    print("Others Error Occured.")
finally:
    print("Done.")

# 2
class SalaryNotInRangeException(Exception):
    pass

salary = [15000, 20000, 10000, 5000]
try:
    for i in salary:
        if (i < 10000 or i > 20000):
            raise SalaryNotInRangeException
        print("Salary:", i)
except SalaryNotInRangeException:
    print("Salary Not In Range Execption Occured.")
except:
    print("Others Error Occured.")
finally:
    print("Done.")

3

class Vehicle:
    def __init__(self, color):
        self.color = color

class Taxi(Vehicle):
    def __init__(self, color):
        super().__init__(color)
        self.__capacity = 0
        self.__model = ""
        self.__variant = ""

    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity
    
    def setVariant(self, variant):
        self.__variant = variant

    def getModel(self):
        return  self.__model
    
    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

ob = Taxi("Red")
ob.setModel("Ak_47")
ob.setCapacity(40)
ob.setVariant("KLR")

print(ob.getCapacity())

# NumPy Array Join

# join 
import numpy as np 
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a = np.concatenate((a1, a2))
print(a)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
arr2 = np.concatenate((arr1, arr2), axis=0)
print(arr)
print(arr2)

# using stack func
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# heapstack

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

# vstack
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

# dstack

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print(arr)

