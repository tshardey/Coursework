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


def ComputingFrequencies(Text, k):
    FrequencyArray = [];
    for i in range(0, 4**k):
        FrequencyArray.append(0)
    for i in range(len(Text)-(k-1)):
        Pattern = Text[i:i+k];
        j = PatternToNumber(Pattern);
        FrequencyArray[j]= FrequencyArray[j]+1;
    standardArray = ' '.join(str(v) for v in FrequencyArray)
    return standardArray
    
import sys # you must import "sys" to read from STDIN
Text, intK = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(intK)

print(ComputingFrequencies(Text,k))