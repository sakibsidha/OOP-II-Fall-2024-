a = (1, 3, 5, 7, 4)

# 1
odd_sum = sum(x for x in a if x % 2 != 0)
print("Sum of all odd numbers:", odd_sum)


# 2
print("Element at index 1:", a[1])
print("Element at index 2:", a[2])
print("Element at index 3:", a[3])


# 3
odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)
print("Number of odd numbers:", odd_count)
print("Number of even numbers:", even_count)


# 4
new_tuple = a + (2, 4, 6)
print("Extended tuple:", new_tuple)


# 5
temp_list = list(a)
temp_list.insert(2, 400)
a = tuple(temp_list)
print("Tuple after adding 400 at index 2:", a)


# 6
a = a[:-1]
print("Tuple after removing last element:", a)


# 7
sliced_tuple = a[-4:-1]
print("Sliced tuple [-4:-1]:", sliced_tuple)


# 8
for x in a:
    if x == 5:
        continue
    print(x, end=" ")
print("")
