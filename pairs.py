l =[23,45,12,2,13,56,77,11,3]

k =5

n = len(l)

for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            print(l[i],l[j])