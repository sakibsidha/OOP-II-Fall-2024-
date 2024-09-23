a = "hello"
b = "b22"
c = "3g    "

# 1
d = a + " " + b + " " + c
print(d)

# 2
print(len(d))
print(d[:-3])
print(d[::-1])

# 3
print(d.upper())
print(d.lower())
print(d.title())
print(d.strip())
print(d.isdigit())
print(d.find("39"))
print(d.find("a2"))
print(d.capitalize())
print(d.isalnum())
print(d.count("2"))
print(d.split())
print(d.replace("hello", "python"))

if("a2" in d):
    print("Yes")
else:
    print("No")

# lamda
x = lambda a, b : a ** b
print(x(2, 5))

# map

def func(a, b):
    return a ** b
    
a = list(map(func, (2, 3, 4), (3, 3, 3)))
print(a)

comp = [10, 3, 5, 6]
newlist = [x for x in comp if x % 2 == 0]

print(newlist)
