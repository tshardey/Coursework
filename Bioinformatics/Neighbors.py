# import sys
# Pattern, strd  = sys.stdin.read().splitlines()
# d = int(strd)

def Neighbors(Pattern, d):
    if d == 0:
        return set([Pattern])
    if len(Pattern) ==1:
        return set(['A', 'C', 'G', 'T'])
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if Hamming(Pattern[1:], Text) <d:
            for nucleotide in set(['A', 'C', 'G', 'T']):
                Neighborhood.add(''.join([nucleotide, Text]))
        else:
             Neighborhood.add(''.join([Pattern[:1], Text]))
    return Neighborhood

def Hamming(Genome1, Genome2):
    count = 0
    for i in range(0, len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count

Pattern = 'ACGT'
d = 3

# ofile = open("NeighborsTest", "w")
# ofile.write('\n'.join(Neighbors(Pattern, d)))

# ofile.close()
print(len(Neighbors(Pattern,d)))
