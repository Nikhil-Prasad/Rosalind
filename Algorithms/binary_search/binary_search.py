# Version that needs to add fiile pasrsing script. The output from rosalind is a file that has two arrays
# and the length of each.
 

def binary_search(target,A):
    low = 0 
    high = len(A) - 1
    # set the half way point, this needs to dynamically update

    while low <= high: 
        half = (low + high)//2
        if A[half] == target:
            return half +1 
        
        elif A[half] > target:
            high = half -1 
        
        elif A[half] < target:
            low = half + 1 
    return -1 

# have to generate list one and two now. 
list1 = [10,20,30,40,50]
list2 = [40,10,35,15,40,20]

for i in range(0, len(list2)):
    #output_list.append(binary_search(list2[i], list1))
    print(binary_search(list2[i], list1))