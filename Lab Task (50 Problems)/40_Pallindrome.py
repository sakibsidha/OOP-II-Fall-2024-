s = input("Enter a string: ")
l = 0
r = len(s)-1
f = 0
while(l <= r):
    if(s[l] != s[r]):
        f = 1
        break
    l += 1
    r -= 1
if(f == 0):
    print("Pallindrome")
else:
    print("Not a pallindrome")