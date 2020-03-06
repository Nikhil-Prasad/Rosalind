# the fibonacci numbers 0,1,1,2,3,5,13,21,34 are generated from fibnoacci rule. Implement recurively. 
# import time 

def fibnoacci_exp(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1 
    else:
        return fibnoacci_exp(number-1) + fibnoacci_exp(number-2)

def fibonacci_linear(number):
    a = 0 
    b = 1 
    for i in xrange(0,number):
        #print("i:" , i)
        #print("a:" , a)
        #print("b:" , b)
        a,b = b, a+b
    return a 

def fibonacci_linear_old(number):
    if number == 0:
        return 0 
    f = [0,1]
    for i in range(2, number+ 1):
        f.append(f[i-1] + f[i-2])
    return f[number]

print(fibonacci_linear(5))
print(fibonacci_linear_old(5))
print(fibnoacci_exp(5))
