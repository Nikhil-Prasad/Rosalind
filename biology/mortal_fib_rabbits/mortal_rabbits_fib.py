def fib(n,m):
    if n < m:
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        elif n == 2: 
            return 1
        else: 
            return fib(n-1,m) + fib(n-2,m)
    elif n == m:
        return fib(n-1,m) + fib(n-2,m) - 1
    else: 
        return fib(n-1,m) + fib(n-2,m) - fib(n-(m+1),m)

print("regular recursion",fib(6,3))

def fib_array(number,month):
    n = number
    m = month                                                                                                        
    rabbits = [1, 1]                                                               
    months = 2                                                                     
    while months < n:                                                              
        if months < m:                                                             
            rabbits.append(rabbits[-2] + rabbits[-1]) 
            print(rabbits)                             
        elif months == m:                                        
            rabbits.append(rabbits[-2] + rabbits[-1] - 1)
            print(rabbits)                          
        else:                                                                      
            rabbits.append(rabbits[-2] + rabbits[-1] - rabbits[-(m + 1)]) 
            print(rabbits)                                                          
        months += 1                                                                
    return rabbits[-1] 

print("fib array",fib_array(91,17))