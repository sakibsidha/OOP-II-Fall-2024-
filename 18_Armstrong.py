num = int(input())

s = str(num)

sum = 0
for i in s:
    cur_digit = int(i)
    mult = 1
    for j in range(len(s)):
        mult = mult * cur_digit

    sum += mult

if(sum == num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")