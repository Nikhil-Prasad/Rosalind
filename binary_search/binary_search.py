# Version that needs to add fiile pasrsing script. The output from rosalind is a file that has two arrays
# and the length of each.
 
with open('rosalind_bins.txt', 'r') as reader:
    line = reader.readlines()
    while line != '': # The EOF char is an empty string 
        print(line, end='')
        line = reader.readline()

