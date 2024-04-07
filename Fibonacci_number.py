def Fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b = b, a+b
f1 = Fibonacci()

print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
