a = [1, 3, 5, 7, 4]

# 1
print("a[2]:", a[2])
print("Length of a:", len(a))
print("Type of a:", type(a))


# 2
a[-3] = 50
print(a[2:4])


# 3
a.append(100)
a.insert(2, 200)
print(a)


# 4
a.pop()
a.pop(1)
print(a)


# 5
b = [2, 4, 6]
a.extend(b)
print("After joining with b, a:", a)


# 6
b = a.copy()
print("New list b (copy of a):", b)


# 7
b.sort()
print("Sorted list b:", b)


# 8
print("Elements in a:")
for element in a:
    print(element, end=" ")
    if element == 5:
        break
print("")


# 9
largest = max(a)
print("Largest number in a:", largest)
