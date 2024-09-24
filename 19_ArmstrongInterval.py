def isArmstrong(num):
    s = str(num)
    sum = 0
    for i in s:
        cur_digit = int(i)
        mult = 1
        for j in range(len(s)):
            mult *= cur_digit
        sum += mult

    if(sum == num):
        return True
    else:
        return False
    
l = int(input())
r = int(input())

for i in range(l, r + 1):
    if(isArmstrong(i) == True):
        print(i, "is an Armstrong Number")
    else:
        print(i, "is not an Armstrong Number")