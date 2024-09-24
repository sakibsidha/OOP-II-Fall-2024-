def f(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return f(a - 1) + f(a - 2)

n = int(input("Enter a number: "))
print("nth fibonacci number is", f(n))