import sys # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines() # read in the input from STDIN

# f = open('dataset_158_9 (1).txt', 'r')
# lines = f.read().splitlines()

# k = int(lines[0])
# DNA = lines[1:]

k = 7
DNA = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC", "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC", "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]

def MedianString(DNA, k):
    distance = float("inf")
    for i in range(0,  4**k-1):
        Pattern = NumberToPattern(i, k)
        if distance > DistanceBetweenPatternStrings(Pattern, DNA):
            distance = DistanceBetweenPatternStrings(Pattern, DNA)
            Median = Pattern
    return Median

def DistanceBetweenPatternStrings(Pattern, DNA):
    k = len(Pattern)
    distance = 0
    for Text in DNA:
        HammingDistance = float("inf")
        for i in range(0, len(Text) - k + 1):
            PatternPrime = Text[i: i+k]
            if HammingDistance > Hamming(Pattern, PatternPrime):
                HammingDistance = Hamming(Pattern, PatternPrime)
        distance += HammingDistance
    return distance
        
def Hamming(Genome1, Genome2):
    count = 0
    for i in range(0, len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count
    
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
    return ''.join(str(v) for v in Pattern)

print(MedianString(DNA, k))