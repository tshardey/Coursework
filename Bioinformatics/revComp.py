#import sys # you must import "sys" to read from STDIN
# dna = sys.stdin.read() # read in the input from STDIN
dna = 'ATGT'
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
    return reverse
    
standardComp = revComp(dna)
print(''.join(standardComp))
