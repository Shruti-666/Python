l = [0,1,2,3]

sum =0

for i in l:
    if i==1:
        raise Exception("Exception: 1 is found")
    else:
        sum +=1
        