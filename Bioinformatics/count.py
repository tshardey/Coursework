def Count(Genome, Pattern, d):
    count =0
    Neighborhood = Neighbors(Pattern, d)
    for item in Neighborhood:  
        for i in range (0, len(Genome) - len(Pattern) + 1):
            if Genome[i: i+len(Pattern)] == item:
                count +=1
    return count 
 
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
        
Genome = 'CGTGACAGTGTATGGGCATCTTT'
Pattern = 'TGT'
d = 1

print(Count(Genome, Pattern, d))