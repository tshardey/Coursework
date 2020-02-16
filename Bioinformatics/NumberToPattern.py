# import sys # you must import "sys" to read from STDIN
# strNumber, strLength = sys.stdin.read().splitlines() # read in the input from STDIN

# Number = int(strNumber);
# length = int(strLength);

Number = 45;
length = 4;

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

patternJoin = NumberToPattern(Number, length)
print(''.join(str(v) for v in patternJoin))
