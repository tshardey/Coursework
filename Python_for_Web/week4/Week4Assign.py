import urllib
import re

from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

tags = soup('span')

numlist = list()

for tag in tags:
   contents = tag.contents[0]
   print contents
   num = float(contents)
   print num
   numlist.append(num)
    
print "Sum:", sum(numlist)
print "Amount:", len(numlist)
