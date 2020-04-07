#enumerating gene orders 
def generate(n):
    l = []
    for number in range (1,n+1):
        l.append(number)
    return l
def permutation(l,n):
    if n == 1:
        return l
    else:
        for element in range (len(l), 0,--):
            l[element] = l[element+1]
            permutation(l,n+1)
            l[element] = l[element+1]
            print(l)

l = generate(5)
permutation(l,5)