import re

stuff = re.findall('[0-9]+' , open('Week2Actual.txt','r').read()) 

num =[float(i) for i in stuff]

print sum(num)