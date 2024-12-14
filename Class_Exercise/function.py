# 1
def cal(a, b):
    return a**2 + b**2 + 2*a*b

a = int(input("a: "))
b = int(input("b: "))
print("Result: ", cal(a, b))


# 2
res = lambda a, b: a**2 + b**2 + 2*a*b

a = int(input("a: "))
b = int(input("b: "))
print("Result:", res(a, b))


# 3
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number: "))
print(f"Factorial of {n} is:", factorial(n))


# 4
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
