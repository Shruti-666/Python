l =[23,45,12,2,13,56,77,11,3]

maximum = l[0]
minimum = l[0]
n = len(l)
for i in range (n) :
    if l[i]> maximum:
        maximum  = l[i]
    if l[i]<minimum :
        minimum = l[i]

print(maximum, minimum)