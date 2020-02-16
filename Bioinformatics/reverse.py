full = [1,1,2,2,1,1,2,2]

def median(element):
    seq = sorted(element)
    if len(seq) % 2 == 0:
        index1 = len(seq)/2
        index2 = index1-1
        num1 = seq[index1]
        num2 = seq[index2]
        avg = (num1 + num2)/ 2.0
        return avg
        print avg
    else:
        index = len(seq)/2 + 0.5
        num = seq[int(index)]
        return num
        print num
        
median(full)