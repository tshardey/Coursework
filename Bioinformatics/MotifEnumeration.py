import sys

def read_file(input_file):
    f = open(input_file)
    data = [item.strip() for item in f.readlines()]
    k,d = map(int,data[0].split(' '))
    f.close()
    return (k,d,data[1:])

k, d, DNA = read_file(sys)

def MotifEnumeration(DNA, k, d):
    DNASet = [None]*len(DNA)
    counter=0
    for text in DNA:
        intNeighbors = list()
        for i in range(0, len(text)- k +1):
            Pattern = text[i:i+k]
            neighbors = Neighbors(Pattern, d)
            for neighbor in neighbors:
                intNeighbors.append(neighbor)
        DNASet[counter] = intNeighbors
        counter += 1
    result = set(DNASet[0])
    for kmer in DNASet[1:]:
        result.intersection_update(kmer)
    return ' '.join(sorted(result))

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

print(MotifEnumeration(DNA, k, d))