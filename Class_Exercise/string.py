a = "hello"
b = "b2b2b2 "
c = " 3g3g "


# 1
d = a + b + c
print("d:", d)


# 2
print("Length of d:", len(d))
print("Reversed d:", d[::-1])


# 3
is_a2_present = "a2" in d
print("Is 'a2' present in d?:", is_a2_present)


# 4
print("Uppercase:", d.upper())
print("Lowercase:", d.lower())
print("Titlecase:", d.title())
print("Stripped:", d.strip())
print("Is digit:", d.isdigit())
print("Index of '3g':", d.find("3g"))
print("Capitalized:", d.capitalize())
print("Is alphanumeric:", d.isalnum)
print("Count of 'b2':", d.count("b2"))
print("Split:", d.split())
print("Swapcase:", d.swapcase())
print("Left strip:", d.lstrip())
print("Replace 'hello' with 'python':", d.replace("hello", "python"))
