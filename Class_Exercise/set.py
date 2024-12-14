a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}


# 1
print("Set a:", a)
print("Set b:", b)


# 2
print("Length of set a:", len(a))
print("Type of set a:", type(a))

print("Length of set b:", len(b))
print("Type of set b:", type(b))


# 3
a.add(10)
print("Set a after adding 10:", a)


# 4
a.discard(8)
print("Set a after removing 8:", a)


# 5
union_set = a.union(b)
print("Union of a and b:", union_set)

intersection_set = a.intersection(b)
print("Intersection of a and b:", intersection_set)

difference_set = a.difference(b)
print("Difference of a - b:", difference_set)

symmetric_difference_set = a.symmetric_difference(b)
print("Symmetric Difference of a and b:", symmetric_difference_set)

is_subset = a.issubset(b)
print("Is set a a subset of set b?", is_subset)

is_subset_reverse = b.issubset(a)
print("Is set b a subset of set a?", is_subset_reverse)


# 6
new_list = [2, 3, 4]
a = a.union(set(new_list))
print("Set a after joining with list [2, 3, 4]:", a)

