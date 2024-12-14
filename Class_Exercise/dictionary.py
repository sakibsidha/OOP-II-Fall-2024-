employee = {
    "name": "A",
    "age": 40,
    "type": {"developer": ["ios", "android"]},
    "permanent": True,
    "salary": 30000,
    100: (1, 2, 3),
    4.5: {5, 6, True, 7, 1}
}

# 1
print("Length of dictionary:", len(employee))
print("Type of employee:", type(employee))


# 2
developer_types = employee["type"]["developer"]
print("Developer types:", developer_types)


# 3
employee["permanent"] = False
print("Updated 'permanent':", employee["permanent"])


# 4
employee["gender"] = "male"
print("Added 'gender':", employee["gender"])


# 5
employee.pop("age")
print("Updated dictionary:", employee)


# 6
print("Keys:", list(employee.keys()))
print("Values:", list(employee.values()))
print("Items:", list(employee.items()))


# 7
print("Iterating dictionary:")
for key, value in employee.items():
    print(f"{key}: {value}")
