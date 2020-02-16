# f = open('dataset_9_4_1.txt', 'r')
import sys 
Pattern, Text, strd= sys.stdin.read().splitlines()

d=int(strd)
def HammingDistance(p, q):
    d = 0
    for p, q in zip(p, q): # your code here
        if p!= q:
            d += 1
    return d

def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    for i in range(len(Text) - len(Pattern)+1):
        # and using distance < d, rather than exact matching
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            positions.append(i)
    return positions

print (' '.join(str(v) for v in ApproximatePatternMatching(Pattern, Text, d)))