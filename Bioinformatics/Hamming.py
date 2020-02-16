#import sys
#Genome1, Genome2  = sys.stdin.read().splitlines()

# f = open('dataset_9_3.txt', 'r')
# Genome1, Genome2 = f.read().splitlines()

def Hamming(Genome1, Genome2):
    count = 0
    for i in range(0, len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count



Genome1 = "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
Genome2 = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"

print(Hamming(Genome1, Genome2))