Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

import math 

def MotifEntropy(Motifs):
    for motif in Motifs:
        count = [0]*len(motif)
        A=0; C=0; G=0; T=0;
        for nuc in motif:
            if nuc == "A":
                A +=1
            elif nuc == "C":
                C += 1
            elif nuc == "G":
                G += 1
            elif nuc == "T":
                T += 1
            count[motif.index(nuc)] = [float(A)/len(motif), float(C)/len(motif), float(G)/len(motif), float(T)/len(motif)] 
    print count
    entropy = [0]*len(count)
    for prob in count:
        for i in range(0, len(prob)):
            try:
                entropy[count.index(prob)] += -1 * (prob[i] * math.log(prob[i], 2))
            except:
                entropy[count.index(prob)] += 0
    return sum(entropy)
    
print(MotifEntropy(Motifs))