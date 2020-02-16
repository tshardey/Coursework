Genome ="CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG"
k = 3
Length = 25
t = 3

print len(Genome)
#f = open('VibChol.txt', 'r')
#Genome = f.read()
#Pattern = "CTTGATCAT"

def BetterClumpFinding(Genome, k, t, Length):
    FrequentPatterns = set();
    Clump = [];
    for i in range(0, (4**k)-1):
        Clump.append(0);
    Text = Genome[i:Length];
    FrequencyArray = ComputingFrequencies(Text, k);
    for i in range(0, (4**k) - 1):
        if FrequencyArray[i] >= t:
            Clump[i] = 1;
    for i in range(1, len(Genome) - Length):
        FirstPattern = Genome[i-1: i-1+k];
        index = PatternToNumber(FirstPattern);
        FrequencyArray[index] = FrequencyArray[index] - 1;
        LastPattern = Genome[i+Length-k: i+Length];
        index = PatternToNumber(FirstPattern);
        FrequencyArray[index] = FrequencyArray[index] + 1;
        if FrequencyArray[index] >= t:
            Clump[index] = 1;
    for i in range(0, 4**k-1):
        if Clump[i] == 1:
            Pattern = NumberToPattern(i, k);
            stanPattern = str(''.join(Pattern))
            FrequentPatterns.add(stanPattern)
    FrequentList = list(FrequentPatterns);
    stdFrequentList = ' '.join(FrequentList)
    return stdFrequentList
              
def ComputingFrequencies(Text, k):
    FrequencyArray = [];
    for i in range(0, 4**k):
        FrequencyArray.append(0)
    for i in range(len(Text)-(k-1)):
        Pattern = Text[i:i+k];
        j = PatternToNumber(Pattern);
        FrequencyArray[j]= FrequencyArray[j]+1;
    return FrequencyArray
        
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
    return Pattern
    
print BetterClumpFinding(Genome, k, t, Length)