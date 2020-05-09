f = open('rosalind_gc.txt', 'r')
string_file =  f.read()#read in as a string so you can use split. 

genes = string_file.split(">")[1:]
gc = []
keys = []

for gene in genes:
    GC_count = gene.count("C") + gene.count("G")
    total_count = gene.count("C") + gene.count("G") + gene.count("A") + gene.count("T")
    gc.append(float(GC_count)*100/total_count)
    keys.append(gene[:13])

print(keys[gc.index(max(gc))])
print(max(gc))
#print(genes[gc.index(max(gc))][:13]) #prints the first 13 character of the gene string in roder 
