n = int(input())

first = 0
second = 1

for i in range (1, n+1):
    cur = first + second
    first = second
    second = cur 

print(second) 

