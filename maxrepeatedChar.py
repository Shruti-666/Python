s = "infinity"

new = {}
n = len(s)
for i in s:
    if i in new:
        new[i] +=1
    else:
        new[i] =1

print(new)

print("max = ", max(new, key = new.get))