def fib(number,k):
    if number == 0:
        return 0
    elif number == 1:
        return 1 
    elif number == 2:
        return 1
    else:
        return fib(number-1,k) + fib(number-2,k) + fib(number-k,k)
print(fib(6,3))