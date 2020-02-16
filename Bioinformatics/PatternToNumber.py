# import sys # you must import "sys" to read from STDIN
# Pattern = sys.stdin.read() # read in the input from STDIN

# Pattern = "";

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

print(PatternToNumber(Pattern))
    