a = int(input("base: "))
b = int(input("power: "))

ans = 1
for i in range(0, b):
    ans *= a

print(ans)