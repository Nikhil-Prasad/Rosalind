#test for learning sorting with bubble sort first. 

def swap(list1,a,b): #something about this gets indexed incorrect when being called. 

    list1[a], list1[b] = list1[b], list1[a]
    return list1

#driver 
#driver = [23,65,19,90]
#pos1, pos2, = 0,1 

#print(driver)
#rint(swap(driver,pos1,pos2))

def bubble_sort(list_1):
    for pass_number in range(len(list_1)-1,0,-1):
        for i in range(pass_number):
            if list_1[i]>list_1[i+1]:
                temp = list_1[i]
                list_1[i] = list_1[i+1]
                list_1[i+1] = temp

driver = [54,26,93,17,77,31,44,55,20]
bubble_sort(driver)
print(driver)
