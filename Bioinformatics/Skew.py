# import sys
# Genome = sys.stdin.read()

f = open('dataset_7_6.txt', 'r')
Genome = f.read()

# Genome ="TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
def Skew(Genome):
    Skew = [0]*(len(Genome)+1);
    for i in range (0, len(Genome)):
        if Genome[i] == "G":
            Skew[i+1] = Skew[i] + 1
        elif Genome[i] == "C":
            Skew[i+1] = Skew[i] -1
        else:
            Skew[i+1] = Skew[i]
    #stdSkew = ' '.join(str(v) for v in Skew)
    return Skew

def MinSkew(Genome):
    Graph = Skew(Genome)
    minPoint = list()
    for i in (i for i,x in enumerate(Graph) if x == min(Graph)):
        minPoint.append(i)
    stdMinPoint = ' '.join(str(v) for v in minPoint)
    return stdMinPoint
    
print(MinSkew(Genome))
