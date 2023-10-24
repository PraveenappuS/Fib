def fib(n):
    a = 0
    b = 1

    if n<0:
        print("Please provide the positive input.")

    elif n==0:
        return a
    
    elif n == 1 or n == 2:
        return b

    else:
        for i in range(1, n+1):
            sum = a+b
            a = b
            b = sum
        return sum
        
f = fib(10)
print(f)
    