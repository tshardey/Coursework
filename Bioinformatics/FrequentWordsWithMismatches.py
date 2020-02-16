import sys
import itertools 
# Pattern, strd  = sys.stdin.read().splitlines()
# d = int(strd)
import numpy as np

Text = 'AGTCAGTC'
k = 4
d = 2

def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = set()
    Neighborhoods = list()
    NeighborhoodInt = []
    for i in range(0, len(Text)-k):
        Neighborhoods.append(Neighbors(Text[i:i+k], d))
    NeighborhoodArray = list(itertools.chain.from_iterable(np.asarray(Neighborhoods)))
    Index = [None]*(len(NeighborhoodArray))
    Count = [None]*(len(NeighborhoodArray))
    for i in range (0, len(NeighborhoodArray)):
        Pattern = NeighborhoodArray[i]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index)
    for i in range(0, len(NeighborhoodArray)-1):
        if SortedIndex[i]== SortedIndex[i+1]:
            Count[i+1] = Count[i] + 1
    maxCount = max(Count)
    for i in range(0, len(NeighborhoodArray)-1):
        if Count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.add(Pattern)
    return ' '.join(sorted(list(FrequentPatterns)))

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

def PatternToNumber(Pattern):
    A = 0; C = 1; G=2; T=3;
    count = [None]*len(Pattern);
    for i in range(0, len(Pattern)):
        if Pattern[i] == "A":
            count[i] = A*(4**(len(Pattern)-i-1));
        elif Pattern[i] == "C":
            count[i] = C*(4**(len(Pattern)-i-1));
        elif Pattern[i] == "G":
            count[i] = G*(4**(len(Pattern)-i-1));
        else:
            count[i] = T*(4**(len(Pattern)-i-1));
    return sum(count)

def NumberToPattern(Number, length):
    count = [None]*(length);
    for i in range(0, length):
        count[i] = Number%4;
        Number = Number/4;
    inverseCount = count[::-1]
    Pattern = [None]*length
    for k in range(0, len(inverseCount)):
        if inverseCount[k] == 0:
            Pattern[k] = "A";
        elif inverseCount[k] == 1:
            Pattern[k] = "C";
        elif inverseCount[k] == 2:
            Pattern[k] = "G";
        elif inverseCount[k] == 3:
            Pattern[k] = "T";
    orderedPattern = ''.join(Pattern)
    return orderedPattern

print(FrequentWordsWithMismatches(Text, k, d))