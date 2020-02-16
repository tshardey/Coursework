#import sys # you must import "sys" to read from STDIN
#Pattern, Genome = sys.stdin.read().splitlines() # read in the input from STDIN

#f = open('VibChol.txt', 'r')
#Genome = f.read()
#Pattern = "CTTGATCAT"

def patPosition(Pattern, Genome):
    position = [];
    for i in range(0, len(Genome)-len(Pattern)+1):
        check = []
        for j in range(i, i+len(Pattern)):
            check.append(Genome[j]);
        redCheck = ''.join(check)
        if redCheck == Pattern:
            position.append(i);
        finalPos = ' '.join(str(e) for e in position)
    return finalPos
    
print(patPosition(Pattern, Genome))   