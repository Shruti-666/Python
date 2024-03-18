def common_letter():
    str1=input("First String: ")
    str2=input("Second STring: ")
    str1 =set(str1)
    str2 = set(str2)

    ans = str1 & str2

    print(ans)

common_letter()