f = open('rosalind_revc.txt', 'r')
sample = f.read()
def complement(s):
    s_c = []
    s = s [::-1]
    for letter in s:
        if letter == "A":
            s_c.append('T')
        if letter == "T":
            s_c.append("A")
        if letter == "G":
            s_c.append("C")
        if letter == "C":
            s_c.append("G")
    s_c_string = ''.join(s_c)
    return s_c_string

#sample = "GAACCAGCGTTACAAGAGAAGCACTCAGCTAAAATTTCGTACCTCTGCGTAGGCCTTCAATGTGTAGGGCGTTCCTCGTGAACCATGGTCATCTTAGATCTTATGACTTACAACACTCCATGTTTTTAACACCTACTCCACCGCTGCTAGCGTGTCGTTGGCTTGCGCCGACCGCCGTGCATTCAAGAAAATCATGAAGCTTGAGTTCTAAAAAGCGGACCCCGAAGTTGGGACTAGTGAGCCACGTCTGTTGCCAGTTACCCGGCATTGATAAGTATAACTTTCCCTCGATTAACGAAATCAGATCATAAATTATAGTGTCTACCCTATGGGATAACTAAGAAAAAGCTGAGGTAAGTTAATCTACTGCGCCGGCCAAACCCCGACGTGCGGAAGATACCGGAGGAATCTCAGGAGTTAGGCTGTTCGCCGGTATCCGTGCCCTTCCGAACAGACGCGTGGTGTCGTAGTTATGTACATGGGTGCAGTGGTCGTGAACGTGATCTGAACATACCAATAACTCGACCTCTTGAGACGGGTCTGCGGAATACCACGGACACGTCCCCTCTAAAACATTCTCAGCAACGCGTGGACGCTTTCAATGTGCAGCGATAACTGAGGCCTAGGGCGCCGGGTTTGGCAAAGAGCGTAACTTGACACCACCAGTCGGGTCAGTACCAATCCAAGCGAAGAGTGTCTGAAGGGCCTAGCTGTGTACCTATTAGTTATTGCCTATTTAACAGGGGATAATATCAATGCCTGAAACGCACGTCTACCGCGGAGAACCCCAGAGAGGATTCACGCTATCTAAAATGTTTAACCCCATCTGCTGAATAATTGTTTTCCCTGGTCTACCTACATTACTCAACTGACAAATAGAATTACATACAATGCGGAAATCTGCGGACTCGGACCATTGCTTCTTTTTAATCAGGCATTGTATGTAGCACGGTCAACCCGCTG"

print(complement(sample))
