# import sys
# Pattern, Text, strd  = sys.stdin.read().splitlines()

# f = open('dataset_9_4.txt', 'r')
# Pattern, Text, strd  = f.read().splitlines()
# d= int(strd)

def ApproximatePatternCount(Text, Pattern, d):
    count = 0;
    for i in range(0, len(Text)-len(Pattern)+1):
        PatternPrime = Text[i : i+ len(Pattern)];
        if Hamming(Pattern, PatternPrime) <= d:
            count += 1;
    return count


def Hamming(Genome1, Genome2):
    count = 0
    for i in range(0, len(Genome1)):
        if Genome1[i] != Genome2[i]:
            count += 1
    return count

#Text = '';
#Pattern = 'CGTAG'
#d =2;

print(ApproximatePatternCount(Text, Pattern, d))
