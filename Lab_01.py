print("Hello World!")

name = "Kh Sadman Sakib"
print(name)

age = 45
salary = 100000

print(age)
print(salary)

complex_var = 1j
print(complex_var)

fl = True
if (fl == True):
    print("Hola!")

# input
val = input("What's your name? ")
print("Your name is " + val)

a = 34
b = 35
add = a + b
sub = a - b 
mul = a * b 
mod = a % b 
exp = a ** b
div = a // b    # integer division
div2 = a / b

print(add)
print(sub)
print(mul)
print(mod)
print(exp)
print(div)
print(div2)

# logical operators
a = True
b = False

print(a and b) # should print False
print(a or b) # should print True
print(not a) # should print False as a is True

a = 5
b = 2

print(a & b) # should print (101 & 010) = 000 = 0
print(~a) # -6
print(a ^ b) # should print (101 ^ 010) = 111 = 7
print(a << 1) # should shift all the bits to the left by 2, so 1010 = 10
print(a >> 1) # opposite, 101 -> 10, so should print 2

# if else

i = 20
if (i%2 == 0):
    print("Even")
else:
    print("Odd")

# will print even
# else if -> elif

n = 10
for i in range (0, n+1, 1):
    print(i, end = " ")

# should print numbers from 0 to 10

count = 0
while (count < 6):
    count = count + 1
    print("Let's Goooo!")

# should print the text 5 times


