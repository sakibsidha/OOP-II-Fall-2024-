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
