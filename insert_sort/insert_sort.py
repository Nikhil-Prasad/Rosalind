def insertSort(list_unsorted):
    count = 0
    for index in range(1,len(list_unsorted)):
        key = list_unsorted[index]
        #print(key)
    
        while index > 0 and list_unsorted[index-1] > key: 
            list_unsorted[index] = list_unsorted[index-1]
            index = index -1 
            count = count + 1 
            list_unsorted[index] = key

        #print(count)
    return(count)
        

        

lines = []
file = open("rosalind_ins.txt")
line2 = file.readlines(2)
print(line2)
        #lines.append(line2) #storing everything in memory!
        #print(lines)

