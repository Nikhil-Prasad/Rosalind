def rabbit_reccurence(number,k):
    if number == 0:
        return 0
    elif number == 1:
        return 1 
    else:
        return rabbit_reccurence(number-1,k) + rabbit_reccurence(number-2,k)*k

print(rabbit_reccurence(5,3))