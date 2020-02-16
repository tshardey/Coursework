import sys # you must import "sys" to read from STDIN
Text, numPattern = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(numPattern)

def PatternCount(Text, Pattern):
    count = 0;
    for i in range(len(Text)):
        if Text[i: i + len(Pattern)] == Pattern:
            count = count +1;
    return count

def FrequentWords(Text, k):
    FrequentPatterns = set();
    Count = list();
    Pattern = list();
    for i in range(0, len(Text)-k+1):
        Pattern.append(Text[i:(i+k)]);
        Count.append(PatternCount(Text, Pattern[i]));
    maxCount = max(Count);
    for i in range(0, len(Text)-k):
        if Count[i]== maxCount:
            FrequentPatterns.add(Pattern[i])
    return FrequentPatterns
    
frequencyList = list(FrequentWords(Text, k));
inverseList = frequencyList[::-1];
print(' '.join(inverseList))
