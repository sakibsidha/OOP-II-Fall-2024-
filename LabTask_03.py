# LIST

a = [1, 3, 5, 7, 4]
# finding length
print("len:", len(a), "type:", type(a))
# accessing indexes
print("a[-2] is", a[-2], "and a[2] is ", a[2])
# changing index values
a[-3] = 50
print("Number at a[-5] is", a[-3])
print(a)
# slicing
print(a[2:4])
print(a[:-3])
print(a[-4:-1])

a.append(100)
a.insert(2, 200)
print("after task 4:", a)
a.pop()
del a[1]
print("after task 5:", a)
a = a + [2, 4, 6]
print("after task 6:", a)
b = a
b.sort()
print(b)
for i in b:
    if i == 7:
        break
    else:
        print(i, end=" ")
print()

a.clear()

#TUPLE

x = (1, 3, 5, 7, 4)
print("len:", len(x), "type:", type(x))
a = list(x)
# accessing indexes
print("a[-2] is", a[-2], "and a[2] is ", a[2])
# changing index values
a[-3] = 50
print("Number at a[-5] is", a[-3])
print(a)
# slicing
print(a[2:4])
print(a[:-3])
print(a[-4:-1])

a.append(100)
a.insert(2, 200)
print("after task 4:", a)
a.pop()
a.pop(1)
print("after task 5:", a)
a.extend([2, 4, 6])
print("after task 6:", a)
b = a
b.sort()
print(b)
for i in b:
    if i == 7:
        break
    else:
        print(i, end=" ")
print()
x = tuple(a)
print(a)


# SET

a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

# len - type
print(len(a), type(a))

# add - remove
a.add(10)
a.remove(8)
print(a)

# union - intersection - difference
c = a | b
print("union:", c)

c = a & b
print("intersection:", c)

c = a - b
print("difference:", c)

# loop
for i in a:
    if i == 5:
        break
    else:
        print(i, end = " ")
print()

# join [2, 3, 4]
x = [2, 3, 4]
x = set(x)
a = a.union(x)
print(a)

# SET

# a = {1, 3, 5, 8, 3, 7}
# b = {0, False, 1, 5}

# print(a, b)

# len - type
# print(len(a), type(a))

# add - remove
# a.add(10)
# a.remove(8)
# print(a)

# union - intersection - difference
# c = a | b
# print("union:", c)
#
# c = a & b
# print("intersection:", c)
#
# c = a - b
# print("difference:", c)

# loop
# for i in a:
#     if i == 5:
#         break
#     else:
#         print(i, end = " ")
# print()

# join [2, 3, 4]
# x = [2, 3, 4]
# x = set(x)
# a = a.union(x)
# print(a)


# DICTIONARY

Employee = {
    "name": "Tanjiro Kamado",
    "age": 40,
    "type":{"developer":["ios", "android"]},
    "permament":True,
    "salary": 30000,
    100 : (1, 2, 3),
    4.5 : {5, 6, True, 7, 1},
}
print(Employee)

# 1
print(len(Employee), type(Employee))

# 2
print(Employee["type"]["developer"])

# 3
Employee["permament"] = False

# 4
Employee["gender"] = "male"

# 5
del Employee["age"]

# 6
for i in Employee.keys():
    print(i, end = " ")
print()

for i in Employee.values():
    print(i, end = " ")
print()

for x, y in Employee.items():
    print(x, y)



