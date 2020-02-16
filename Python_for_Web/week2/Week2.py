# "import re" - Put at the beginning 
# re.search()
# re.find()
# re.findall()

# Standard way of searching through a text to find a string of characters

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line
        
# Same code written as a regular expression

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print line
        
# . The dot character matches any character
# If you add the asterisk character, the character is "any number of times"

# The re.search() returns a True/False depending on whether the string matches the regular expression
# If we actually want the matching strings to be extracted, we use re.findall()

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+' ,x) 
print y

# ['2', '19', '42']

y = re.findall('[AEIOU]+' ,x)
print y

# []

# REGULAR EXPRESSIONS PART 2
 
import re

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
    
print 'Maximum:', max(numlist)

# If you want a special character to be a regular character put a \ before
