def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    return a / b

print("What operation do you want to do?")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Division")

t = int(input())

if(t == 1):
    a = int(input("Add first number: "))
    b = int(input("Add second number: "))
    print("Addition result:", add(a, b))
elif(t == 2):
    a = int(input("Add first number: "))
    b = int(input("Add second number: "))
    print("Substraction result:", subtract(a, b))
elif(t == 3):
    a = int(input("Add first number: "))
    b = int(input("Add second number: "))
    print("Multiplication result:", mult(a, b))
else:
    a = int(input("Add first number: "))
    b = int(input("Add second number: "))
    print("Division result", add(a, b))