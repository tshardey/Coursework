import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN

# f = open('dataset_5164_1.txt', 'r')
# lines = f.read().splitlines()

Pattern = lines[0]
DNA = lines[1].split(" ")

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
    


print(DistanceBetweenPatternStrings(Pattern, DNA))