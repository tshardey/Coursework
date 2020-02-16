import numpy as np
import sys
from operator import mul

# lines = sys.stdin.read().splitlines() 

f = open('dataset_159_3.txt', 'r')
lines = f.read().splitlines()
Text = str(lines[0])
prob = np.matrix([map(float, l.split(" ")) for l in lines[2:]])

def Profile(Text, prob):
    k = prob.shape[1]
    desiredProb = 0
    for i in range(0, len(Text) - k + 1):
        Pattern = Text[i : i+k]
        ProbTotal = 1
        for j in range(0, len(Pattern)):
            if Pattern[j] == "A":
                row = 0
            elif Pattern[j] == "C":
                row = 1
            elif Pattern[j] == "G":
                row = 2
            elif Pattern[j] == "T":
                row = 3
            ProbValue = prob[row, j]
            ProbTotal  *= ProbValue
        if ProbTotal > desiredProb:
            desiredProb = ProbTotal
            Median = Pattern
    return Median
    
print(Profile(Text, prob))