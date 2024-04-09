##using Split method
def palindrome(s):
    temp = s[::-1]
    if temp==s:
        return True
    return False

s = "abba"
print(palindrome(s))

##using for loop
def Palindrome2(s):
    n = len(s)
    for i in range(n):
        if s[i]!=s[n-i-1]:
            return False
    return True
    
print(Palindrome2(s))

##by using reversed an join (in-built function)
def Palindrome3(s):
    reversed_s= reversed(s)
    temp = ''.join(reversed_s)
    if temp==s:
        return True
    return False

print(Palindrome3(s))


##by using while Loop
def Palindrome4(s):
    n = len(s)
    start=0
    end =n-1
    while(start<end):
        if s[start]==s[end]:
            start+=1
            end -=1
        else:
            return False
    return True

print(Palindrome4(s))