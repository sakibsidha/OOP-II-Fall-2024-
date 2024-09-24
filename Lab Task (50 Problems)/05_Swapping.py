a = 5
b = 9

print("before swapping, a:", a, "b:", b)

temp = a
a = b
b = temp

print("after swapping, a:", a, "b:", b)

# We can also swap without using a temporary variable like below:

a = 7
b = 8

a = a + b
b = a - b
a = a - b

