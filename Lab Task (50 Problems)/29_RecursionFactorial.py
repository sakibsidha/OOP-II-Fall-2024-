def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", f(num))