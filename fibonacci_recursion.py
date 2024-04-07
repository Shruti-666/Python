def Fibonacci_recur(n):
    if n <=1:
        return n
    else:
        return (Fibonacci_recur(n-1)+Fibonacci_recur(n-2))
    

for i in range(10):
    print(Fibonacci_recur(i))