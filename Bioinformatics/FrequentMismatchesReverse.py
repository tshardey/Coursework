import sys

# s, stk, strd= sys.stdin.read().splitlines()
# k=int(strk)
# d=int(strd)
s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1

        
def frequentWordsWithMismatchesandReverse( s, k, d ):
    counts = {}
    for i in xrange(len(s)-k+1):
        for sub in [s[i:i+k],revComp(s[i:i+k])]:
            for neighbor in neighbors(s[i:i+k],d):
                if neighbor not in counts:
                    counts[neighbor] = 0
                counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamming( s, t ):
    return sum([s[i] != t[i] for i in xrange(len(s))])

def revComp(dna):
    pair = [None]*len(dna)
    for i in range(0, len(dna)):
        if dna[i] == "A":
            pair[i] = "T";
        elif dna[i] == "T":
            pair[i] = "A";
        elif dna[i] == "G":
            pair[i] = "C";
        else:
            pair[i] = "G"
    reverse = pair[::-1];
    return ''.join(reverse)
    
print frequentWordsWithMismatchesandReverse(s,k,d)