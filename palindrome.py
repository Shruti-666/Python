s = "acbbca"

if (s == s[::-1]):
    print("yes")
else:
    print("no")



##alternate way
n = len(s)
x=0
for i in range(n):
    if s[i]!=s[n-i-1]:
        x =1
        break

if(x==0):
    print("yes palindrome")
else:
    print("no palindrome")